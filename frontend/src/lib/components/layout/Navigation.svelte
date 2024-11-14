<script lang="ts">
	import WorkspaceSelector from './navigation/WorkspaceSelector.svelte';
	import logo from '$lib/assets/logo.png';
	import { Activity, CheckCircle, Database, Eye, Loader } from 'lucide-svelte';
	import { Button } from '../ui/button';
	import { page } from '$app/stores';
	import { cn } from '$lib/utils';
	import { createQuery } from '@tanstack/svelte-query';
	import axios from 'axios';
	import { baseURL } from '$lib/globals';

	const statusQuery = createQuery({
		queryKey: ['status'],
		queryFn: () => axios.get(`${baseURL}/status`),
		refetchOnMount: true
	});

	const status = $derived(
		$statusQuery.isSuccess
			? $statusQuery.data?.data
			: {
					profiling: true,
					cleaning: true,
					deploy: true
				}
	);

	let pages = $derived([
		{ label: 'Dashboard', to: '/', icon: Activity, strict: true },
		{ label: 'Sources', to: '/source', icon: Database },
		{ label: 'Profiling', to: '/profile', icon: Eye, disabled: status['profiling'] },
		{ label: 'Cleaning', to: '/clean', icon: Loader, disabled: status['cleaning'] },
		{ label: 'Deploy', to: '/deploy', icon: CheckCircle, disabled: status['deploy'] }
	]);

	let currentPage = $derived((e: string, strict?: boolean) => {
		if (strict) {
			return $page.url.pathname == e;
		}
		return $page.url.pathname.startsWith(e);
	});
</script>

<section class="flex flex-col gap-2">
	<span class="flex flex-row gap-3">
		<img src={logo} class="h-12 w-12 grayscale invert dark:invert-0" alt="Clarifier Logo" />
		<span class="ml-auto flex flex-col items-end justify-center gap-0">
			<h1 class="font-display m-0 p-0 text-xl font-semibold">Clarifier</h1>
			<h6 class="-mt-.5 text-sm text-primary">Workbench</h6>
		</span>
	</span>
</section>

<WorkspaceSelector />

<section class="flex flex-col gap-0">
	{#each pages as { label, to, icon, strict, disabled }}
		<Button
			size="sm"
			href={to}
			variant={currentPage(to, strict ?? false) ? 'secondary' : 'ghost'}
			class={cn(
				'flex flex-row justify-start gap-3',
				disabled && 'pointer-events-none text-gray-500'
			)}
		>
			{@const SvelteComponent = icon}
			<SvelteComponent size="18" />
			{label}
		</Button>
	{/each}
</section>
