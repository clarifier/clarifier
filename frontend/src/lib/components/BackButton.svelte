<script lang="ts">
	import { ArrowLeftCircle } from 'lucide-svelte';
	import type { ComponentType } from 'svelte';
	import type { Icon } from 'lucide-svelte';

	interface Props {
		text?: string;
		backIcon?: ComponentType<Icon>;
		icon?: ComponentType<Icon>;
		href: any;
	}

	let {
		text = 'Back',
		backIcon = ArrowLeftCircle,
		icon = ArrowLeftCircle,
		href
	}: Props = $props();

	const SvelteComponent = $derived(backIcon);
	const SvelteComponent_1 = $derived(icon);
</script>

<a
	{href}
	class="group flex h-16 w-16 max-w-xs flex-row items-center justify-between gap-4 truncate rounded-md border border-secondary bg-secondary p-5 text-secondary transition-all hover:w-full hover:border-primary hover:text-primary"
>
	<SvelteComponent class="block shrink-0 text-primary group-hover:hidden" />
	<SvelteComponent_1 class="hidden shrink-0 text-primary group-hover:block" />
	<span class="font-semibold">{text}</span>
</a>
