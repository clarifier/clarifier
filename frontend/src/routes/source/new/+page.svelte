<script>
	import BackButton from '$lib/components/BackButton.svelte';
	import { ArrowLeftCircle, Database } from 'lucide-svelte';

	let source = {
		id: '1',
		name: 'Iris',
		description: 'Dataset with Iris Data',
		size: '2 MiB',
		type: 'parquet',
		source: 'OpenML'
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
	<section class="grid grid-cols-2 gap-2 md:grid-cols-3 lg:grid-cols-4"></section>
</main>
