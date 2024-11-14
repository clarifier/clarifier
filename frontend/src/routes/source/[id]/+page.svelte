<script lang="ts">
	import { page } from '$app/stores';
	import BackButton from '$lib/components/BackButton.svelte';
	import { baseURL } from '$lib/globals';
	import { createQuery } from '@tanstack/svelte-query';
	import axios from 'axios';
	import { Database } from 'lucide-svelte';
	import { derived } from 'svelte/store';
	import type { Source } from '$lib/types/source';

	let { params } = $page;

	const sourceQuery = createQuery({
		queryKey: ['source', params.id],
		queryFn: () => axios.get<Source>(`${baseURL}/sources/${params.id}`),
		enabled: params.id != undefined
	});

	const title = derived(sourceQuery, (v) =>
		v.isSuccess ? `${v.data?.data?.name} (${params.id})` : `... ${params.id}`
	);
</script>

<svelte:head>
	<title>Source - {$title} - Clarifier</title>
</svelte:head>

<main class="flex flex-col gap-4">
	<section class="flex h-16 flex-row items-center gap-4">
		<BackButton icon={Database} text="Back to Sources" href="/source" />
		<section class="flex flex-col">
			<h1 class="text-xl font-semibold">{$title}</h1>
			<h2 class="text-lg">Source Details</h2>
		</section>
	</section>
	<section class="flex flex-col gap-4">
		{#if $sourceQuery.isLoading}
			<p>Loading...</p>
		{:else if $sourceQuery.isError}
			<p class="text-red-500">Error loading source data</p>
		{:else if $sourceQuery.isSuccess}
			{@const source = $sourceQuery.data?.data}
			<div class="rounded-md p-4">
				<p><strong>ID:</strong> {source.id}</p>
				<p><strong>Name:</strong> {source.name}</p>
				<p><strong>Description:</strong> {source.description}</p>
				<p><strong>Size:</strong> {source.size}</p>
				<p><strong>Type:</strong> {source.type}</p>
				<p><strong>Source:</strong> {source.source}</p>
				{#if source.data}
					<p><strong>Status:</strong> {source.data.status}</p>
					{#if source.data.ch_table}
						<p><strong>Clickhouse Table:</strong> {source.data.ch_table}</p>
					{/if}
				{/if}
			</div>
		{/if}
	</section>
</main>
