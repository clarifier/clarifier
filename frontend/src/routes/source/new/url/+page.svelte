<script lang="ts">
	import BackButton from '$lib/components/BackButton.svelte';
	import { CirclePlus, CloudDownload } from 'lucide-svelte';
</script>

<svelte:head>
	<title>New Source (Download) - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={CirclePlus} text="Back to New Source" href="/source/new" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">New Source: Download URL</h1>
			<h2 class="text-lg">Download URL to Data Sources</h2>
		</section>
	</section>
</main>
