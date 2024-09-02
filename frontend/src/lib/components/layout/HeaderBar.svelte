<script>
	import Button from '../ui/button/button.svelte';

	import Sun from 'lucide-svelte/icons/sun';
	import Moon from 'lucide-svelte/icons/moon';

	import { toggleMode } from 'mode-watcher';
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

	<Button on:click={toggleMode} variant="outline" size="icon">
		<Sun
			class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
		/>
		<Moon
			class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
		/>
		<span class="sr-only">Toggle theme</span>
	</Button>
</header>
