<script>
	import '../app.css';
	import Navigation from '$lib/components/layout/Navigation.svelte';
	import HeaderBar from '$lib/components/layout/HeaderBar.svelte';
	import Command from '$lib/components/search/Command.svelte';
	import { ModeWatcher } from 'mode-watcher';
	import { QueryClient, QueryClientProvider } from '@tanstack/svelte-query';
	import { browser } from '$app/environment';
	import { Toaster } from '$lib/components/ui/sonner';

	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
			}
		}
	});
</script>

<QueryClientProvider client={queryClient}>
	<Toaster />

	<ModeWatcher />

	<div class="flex h-full min-h-screen w-full flex-row">
		<nav class="flex h-full w-[18em] flex-col gap-4 border-r border-r-secondary p-4">
			<Navigation />
		</nav>
		<section class="flex h-full w-full flex-col gap-4 p-4">
			<HeaderBar />
			<slot />
		</section>
	</div>

	<Command />
</QueryClientProvider>
