<script lang="ts">
	import { ArrowLeftCircle } from 'lucide-svelte';
	import type { ComponentType } from 'svelte';
	import type { Icon } from 'lucide-svelte';

	export let text = 'Back';
	export let backIcon: ComponentType<Icon> = ArrowLeftCircle;
	export let icon: ComponentType<Icon> = ArrowLeftCircle;
	export let href;
</script>

<a
	{href}
	class="group flex h-16 w-16 max-w-xs flex-row items-center justify-between gap-4 truncate rounded-md border border-secondary bg-secondary p-5 text-secondary transition-all hover:w-full hover:border-primary hover:text-primary"
>
	<svelte:component this={backIcon} class="block shrink-0 text-primary group-hover:hidden" />
	<svelte:component this={icon} class="hidden shrink-0 text-primary group-hover:block" />
	<span class="font-semibold">{text}</span>
</a>
