<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { Database } from 'lucide-svelte';
	import * as Select from '$lib/components/ui/select';
	import { sources } from '$lib/components/sources/search';

	let source: {
		value: keyof typeof sources;
		label: string;
		disabled: boolean;
	} = {
		value: 'upload',
		label: sources['upload'].label,
		disabled: false
	};
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

	<section class="flex flex-col gap-1.5">
		<Select.Root portal={null} bind:selected={source}>
			<Select.Trigger class="w-full">
				<Select.Value placeholder="Select how you want to add a new source" />
			</Select.Trigger>
			<Select.Content>
				<Select.Group>
					{#each Object.entries(sources) as [value, { label }]}
						<Select.Item {value} {label}>{label}</Select.Item>
					{/each}
				</Select.Group>
			</Select.Content>
			<Select.Input name="type" />
		</Select.Root>
	</section>

	{#each Object.entries(sources) as [value, { component }]}
		<section class:hidden={value == source?.value}>
			<svelte:component this={component} />
		</section>
	{/each}
</main>
