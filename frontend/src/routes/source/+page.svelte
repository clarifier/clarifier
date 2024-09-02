<script>
	import NewSource from '$lib/components/sources/NewSource.svelte';
	import SourceCard from '$lib/components/sources/SourceCard.svelte';
	import { Database } from 'lucide-svelte';

	let sources = [
		{
			id: '1',
			name: 'Iris',
			description: 'Dataset with Iris Data',
			size: '2 MiB',
			type: 'parquet',
			source: 'OpenML'
		},
		{
			id: '2',
			name: 'Titanic',
			description: 'Passenger survival data from the Titanic',
			size: '1.2 MiB',
			type: 'csv',
			source: 'Kaggle'
		},
		{
			id: '3',
			name: 'MNIST',
			description: 'Handwritten digit images for classification',
			size: '12 MiB',
			type: 'gz',
			source: 'TensorFlow'
		},
		{
			id: '4',
			name: 'Wine Quality',
			description: 'Wine quality data based on physicochemical tests',
			size: '50 KiB',
			type: 'csv',
			source: 'UCI Machine Learning Repository'
		},
		{
			id: '5',
			name: 'Weather Data',
			description: 'Daily weather observations over a decade',
			size: '10 GiB',
			type: 'parquet',
			source: 'NOAA'
		},
		{
			id: '6',
			name: 'COCO',
			description: 'Common Objects in Context dataset for object detection',
			size: '25 GiB',
			type: 'zip',
			source: 'COCO Dataset'
		}
	];
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
	</section>
	<section class="grid grid-cols-2 gap-2 md:grid-cols-3 lg:grid-cols-4">
		{#each sources as source}
			<SourceCard {source} />
		{/each}
		<NewSource />
	</section>
</main>
