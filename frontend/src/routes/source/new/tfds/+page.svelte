<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { CirclePlus, CloudDownload } from 'lucide-svelte';
</script>

<svelte:head>
	<title>New Source (PostgreSQL) - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={CirclePlus} text="Back to New Source" href="/source/new" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">New Source: TensorFlow</h1>
			<h2 class="text-lg">Add TensorFlow Datasource</h2>
		</section>
	</section>
</main>
