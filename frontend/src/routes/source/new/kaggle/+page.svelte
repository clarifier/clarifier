<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { CirclePlus, ExternalLink, Heart, Save } from 'lucide-svelte';
	import * as Card from '$lib/components/ui/card';
	import { searchKaggle, addKaggleSource } from './kaggle';
	import type { KaggleSource } from './kaggle';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Loader, toast } from 'svelte-sonner';
	import { Badge } from '$lib/components/ui/badge';
	import { cn } from '$lib/utils';
	import { Button } from '$lib/components/ui/button';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { goto } from '$app/navigation';
	let search = $state('');
	let selected: KaggleSource = $state();

	const upload = createMutation({
		mutationFn: addKaggleSource,
		onSuccess: ({ data }) => {
			toast.success(`Added Kaggle source ${selected.datasetInfo.datasetSlug}`);
			goto(`/source/${data.id}`);
		},
		onError: () => {
			toast.error(`Adding Kaggle source failed`);
		}
	});

	let query = $derived(createQuery({
		queryKey: ['kaggle', 'search', search],
		queryFn: () => searchKaggle(search)
	}));
</script>

<svelte:head>
	<title>New Source (Kaggle) - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={CirclePlus} text="Back to New Source" href="/source/new" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">New Source: Kaggle</h1>
			<h2 class="text-lg">Add Kaggle Datasource</h2>
		</section>
		<Button
			on:click={() => {
				!!selected && $upload.mutate(selected);
			}}
			variant="secondary"
			class="ml-auto flex h-full flex-row gap-1"
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
				{#each $query.data.data?.documents ?? [] as _source}
					<button class="group transition" onclick={() => (selected = _source)}>
						<Card.Root
							class={cn(
								'flex h-full w-full flex-col justify-between group-hover:border-primary group-hover:shadow-md',
								_source.id == selected?.id && 'border-primary shadow-md'
							)}
						>
							<Card.Header>
								<Card.Title class="flex flex-row items-center justify-between">
									{_source.name}
									<button onclick={(e) => e.stopPropagation()}>
										<Button
											title="Open on Kaggle"
											variant="outline"
											href={`https://www.kaggle.com/datasets/${_source.authorSlug}/${_source.datasetInfo.datasetSlug}`}
											target="_blank"
										>
											<ExternalLink size={12} />
										</Button>
									</button>
								</Card.Title>
								<Card.Description title={_source.id} class="truncate">
									{_source.id}
								</Card.Description>
							</Card.Header>
							<Card.Footer class="flex flex-row flex-wrap gap-1 font-mono text-xs"></Card.Footer>
						</Card.Root>
					</button>
				{/each}
			{/if}
		</section>
	</section>
</main>
