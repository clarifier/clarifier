<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { Database } from 'lucide-svelte';
	import { sources } from './sources';
	import * as Card from '$lib/components/ui/card';
</script>

<svelte:head>
	<title>New Source - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={Database} text="Back to Sources" href="/source" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">New Source</h1>
			<h2 class="text-lg">Add a new source to clean or use data from.</h2>
		</section>
	</section>

	<section class="grid grid-cols-2 gap-2 md:grid-cols-3 lg:grid-cols-4">
		{#each Object.entries(sources) as [page, { icon, description, title }]}
			<a href={`/source/new/${page}`} class="group transition">
				<Card.Root
					class="flex h-full w-full flex-col justify-between group-hover:border-primary group-hover:shadow-md"
				>
					<Card.Header>
						<Card.Title>{title}</Card.Title>
						<Card.Description>{description}</Card.Description>
					</Card.Header>
					<Card.Footer class="flex flex-row flex-wrap gap-1 font-mono text-xs">
						<svelte:component this={icon} />
					</Card.Footer>
				</Card.Root>
			</a>
		{/each}
	</section>
</main>
