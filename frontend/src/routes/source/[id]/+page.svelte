<script lang="ts">
	import { page } from '$app/stores';
	import { baseURL } from '$lib/globals';
	import { createQuery } from '@tanstack/svelte-query';
	import axios from 'axios';

	let { params } = $page;

	const sourceQuery = createQuery({
		queryKey: ['source', params.id],
		queryFn: () => axios.get(`${baseURL}/sources/${params.id}`),
		enabled: params.id != undefined
	});
</script>

{#if $sourceQuery.isLoading}
	Loading...
{:else if $sourceQuery.isError}
	{@const error = $sourceQuery.data?.data}
	{JSON.stringify(error)}
{:else if $sourceQuery.isSuccess}
	{@const source = $sourceQuery.data?.data}
	{JSON.stringify(source)}
{/if}
