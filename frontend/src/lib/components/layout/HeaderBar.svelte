<script>
	import Button from '../ui/button/button.svelte';
	import { searchOpen } from '$lib/stores/search';
</script>

<header class="flex w-full flex-row gap-1">
	<Button
		variant="outline"
		class="relative w-full justify-start text-sm text-muted-foreground sm:pr-12"
		on:click={() => searchOpen.set(true)}
	>
		<span class="inline-flex">Search...</span>
		<kbd
			class="pointer-events-none absolute right-2 top-2 hidden h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium opacity-100 sm:flex"
		>
			<span class="text-xs">⌘</span>K
		</kbd>
	</Button>
</header>
