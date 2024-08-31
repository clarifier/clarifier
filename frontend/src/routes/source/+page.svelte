<script>
	import { Database } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Sources - Clarifier</title>
</svelte:head>

<main>
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
</main>
