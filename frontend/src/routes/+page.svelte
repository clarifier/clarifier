<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { CheckCircle, Database, Eye, Loader } from 'lucide-svelte';

	let pages = [
		{
			title: 'Add a source',
			description: 'Add a CSV file or OpenML source to begin.',
			to: '/',
			icon: Database,
			active: true
		},
		{
			title: 'Select cleaning dimensions',
			description: 'Choose a cleaning framework and align built-in algorithms to your data.',
			to: '/',
			icon: Eye,
			active: false
		},
		{
			title: 'Clean the data',
			description:
				'Organize workflows and use machine learning to clean data on configured dimensions.',
			to: '/',
			icon: Loader,
			active: false
		},
		{
			title: 'Deploy to production',
			description:
				'Export notebooks for manual refinement or convert workflows for continuous use.',
			to: '/',
			icon: CheckCircle,
			active: false
		}
	];
</script>

<svelte:head>
	<title>Dashboard - Clarifier</title>
</svelte:head>

<main>
	<section class="flex w-full flex-col gap-6 rounded-md bg-secondary p-6">
		<section class="flex flex-col">
			<h1 class="text-2xl font-semibold">Get started with Clarifier</h1>
			<h2 class="text-xl">Four steps to clean your data</h2>
		</section>
		<section class="grid grid-cols-2 gap-4 lg:grid-cols-4">
			{#each pages as { title, description, to, icon, active }}
				<section class="flex flex-col gap-4 rounded-md bg-white p-6" class:disabled={!active}>
					<h1 class="font-semibold">{title}</h1>
					<span class="text-sm">{description}</span>
					{#if active}
						<Button href={to} class="mt-auto">
							<svelte:component this={icon} />
						</Button>
					{:else}
						<Button class="mt-auto" disabled>
							<svelte:component this={icon} />
						</Button>
					{/if}
				</section>
			{/each}
		</section>
	</section>
</main>

<style lang="postcss">
	.disabled {
		@apply pointer-events-none text-gray-400;
	}
</style>
