<script lang="ts">
	import NewSource from '$lib/components/sources/NewSource.svelte';
	import SourceCard from '$lib/components/sources/SourceCard.svelte';
	import { ArrowUp, Database, PlusCircle } from 'lucide-svelte';
	import { sourceTypes } from './new/sources';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';

	let sources: any[] = [];
</script>

<svelte:head>
	<title>Sources - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<span
			class="flex aspect-square h-16 w-16 items-center justify-center rounded-md bg-secondary text-primary"
		>
			<Database />
		</span>
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">Sources</h1>
			<h2 class="text-lg">Add sources to clean, wrangle and transform for analysis.</h2>
		</section>
		<DropdownMenu.Root>
			<DropdownMenu.Trigger class="ml-auto h-full">
				<Button variant="outline" class="flex h-full flex-row gap-2">
					<PlusCircle size={18} />
					Add a new source</Button
				>
			</DropdownMenu.Trigger>
			<DropdownMenu.Content>
				<DropdownMenu.Group>
					{#each Object.entries(sourceTypes) as [key, sourceType]}
						<DropdownMenu.Item
							class="flex cursor-pointer flex-row gap-2"
							href={`/source/new/${key}`}
						>
							<svelte:component this={sourceType.icon} size={18} />
							{sourceType.title}
						</DropdownMenu.Item>
					{/each}
				</DropdownMenu.Group>
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</section>
	{#if !sources.length}
		<section class="relative flex w-full items-center justify-center p-3">
			No sources as of yet, add a source!
			<ArrowUp class="absolute right-1 top-1 md:right-4" />
		</section>
	{/if}
	<section class="grid grid-cols-2 gap-2 md:grid-cols-3 lg:grid-cols-4">
		{#each sources as source}
			<SourceCard {source} />
		{/each}
	</section>
</main>
