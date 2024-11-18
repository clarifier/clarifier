<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import { baseURL } from '$lib/globals';
	import { createQuery } from '@tanstack/svelte-query';
	import { workspace } from '$lib/stores/workspace';
	import axios from 'axios';
	import { BriefcaseBusiness, Loader2 } from 'lucide-svelte';

	const workspaceQuery = createQuery({
		queryKey: ['workspaces'],
		queryFn: () => axios.get(`${baseURL}/workspaces/`)
	});
</script>

<Select.Root
	onSelectedChange={(v) => {
		v && workspace.set(v);
	}}
	selected={$workspace}
>
	<Select.Trigger>
		<BriefcaseBusiness />
		<Select.Value placeholder="Workspace" />
	</Select.Trigger>
	<Select.Content>
		{#if $workspaceQuery.isLoading}
			<Select.Item value="loading" disabled><Loader2 class="animate-spin" /></Select.Item>
		{:else if $workspaceQuery.isError}
			<Select.Item value="error" disabled><Loader2 class="animate-spin" /></Select.Item>
		{:else}
			{@const workspaces = $workspaceQuery.data?.data?.items ?? []}
			{#each workspaces as { name, description }}
				<Select.Item value={name}>{description}</Select.Item>
			{/each}
		{/if}
	</Select.Content>
</Select.Root>
