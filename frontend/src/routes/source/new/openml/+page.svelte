<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { CirclePlus, ExternalLink, Heart, Save } from 'lucide-svelte';
	import * as Card from '$lib/components/ui/card';
	import { searchOpenML, addOpenMLSource } from './openml';
	import type { OpenMLSource } from './openml';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Loader, toast } from 'svelte-sonner';
	import { Badge } from '$lib/components/ui/badge';
	import { cn } from '$lib/utils';
	import { Button } from '$lib/components/ui/button';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { goto } from '$app/navigation';
	let search = '';
	let selected: OpenMLSource;

	const upload = createMutation({
		mutationFn: addOpenMLSource,
		onSuccess: ({ data }) => {
			toast.success(`Added OpenML source ${selected.name}`);
			goto(`/source/${data.id}`);
		},
		onError: () => {
			toast.error(`Adding OpenML source failed`);
		}
	});

	$: query = createQuery({
		queryKey: ['openml', 'search', search],
		queryFn: () => searchOpenML(search)
	});
</script>

<svelte:head>
	<title>New Source (OpenML) - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={CirclePlus} text="Back to New Source" href="/source" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">New Source: OpenML</h1>
			<h2 class="text-lg">Add OpenML Datasource</h2>
		</section>
		<Button
			on:click={() => {
				!!selected && $upload.mutate(selected);
			}}
			variant="secondary"
			class={cn(['ml-auto flex h-full flex-row gap-1', selected && 'ring ring-primary'])}
			disabled={!selected}
		>
			<Save />
			Download
		</Button>
	</section>
	<section class="flex flex-col gap-4">
		<section class="flex flex-col gap-2">
			<Label>Search</Label>
			<Input bind:value={search} />
		</section>
		<section class="grid grid-cols-3 gap-2">
			{#if $query.isLoading}
				<Loader visible />
			{:else if $query.isError}
				{$query.error.message}
			{:else if $query.isSuccess}
				{#each $query.data.data?.hits?.hits ?? [] as { _source }}
					<button class="group transition" on:click={() => (selected = _source)}>
						<Card.Root
							class={cn(
								'flex h-full w-full flex-col justify-between group-hover:border-primary group-hover:shadow-md',
								_source.data_id == selected?.data_id && 'border-primary shadow-md'
							)}
						>
							<Card.Header>
								<Card.Title class="flex flex-row items-center justify-between">
									{_source.name}
									<button on:click={(e) => e.stopPropagation()}>
										<Button
											title="Open on OpenML"
											variant="outline"
											href={`https://openml.org/search?type=data&status=active&id=${_source.data_id}`}
											target="_blank"
										>
											<ExternalLink size={12} />
										</Button>
									</button>
								</Card.Title>
								<Card.Description title={_source.data_id} class="truncate">
									{_source.data_id}
								</Card.Description>
							</Card.Header>
							<Card.Footer class="flex flex-row flex-wrap gap-1 font-mono text-xs">
								<Badge variant="outline"><Heart size={8} />&nbsp;{_source.nr_of_likes}</Badge>
								<Badge variant="outline">{_source.date}</Badge>
								<Badge variant="outline">Version&nbsp;{_source.version}</Badge>
							</Card.Footer>
						</Card.Root>
					</button>
				{/each}
			{/if}
		</section>
	</section>
</main>
