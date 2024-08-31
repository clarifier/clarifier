<script lang="ts">
	import WorkspaceSelector from './navigation/WorkspaceSelector.svelte';
	import logo from '$lib/assets/logo.png';
	import { Activity, CheckCircle, Database, Eye, Loader } from 'lucide-svelte';
	import { Button } from '../ui/button';

	let pages = [
		{ label: 'Dashboard', to: '/', icon: Activity },
		{ label: 'Sources', to: '/', icon: Database },
		{ label: 'Profiling', to: '/', icon: Eye },
		{ label: 'Cleaning', to: '/', icon: Loader },
		{ label: 'Deploy', to: '/', icon: CheckCircle }
	];
</script>

<section class="flex flex-col gap-2">
	<span class="flex flex-row gap-2">
		<img src={logo} class="h-12 w-12" alt="Clarifier Logo" />
		<span class="ml-auto flex flex-col items-end justify-center gap-0">
			<h1 class="text-xl text-primary">Clarifier</h1>
			<h6 class="text-xs text-primary">v0.0.1</h6>
		</span>
	</span>
</section>

<WorkspaceSelector />

<section class="flex flex-col gap-0">
	{#each pages as { label, to, icon }}
		<Button size="sm" href={to} variant="ghost" class="flex flex-row justify-start gap-3">
			<svelte:component this={icon} size="18" />
			{label}
		</Button>
	{/each}
</section>
