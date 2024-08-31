<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import { BriefcaseBusiness } from 'lucide-svelte';

	let workspaces = [{ label: 'Default Workspace', value: 'workspace' }];
</script>

<Select.Root selected={workspaces[0]}>
	<Select.Trigger>
		<BriefcaseBusiness />
		<Select.Value placeholder="Workspace" />
	</Select.Trigger>
	<Select.Content>
		{#each workspaces as { value, label }}
			<Select.Item {value}>{label}</Select.Item>
		{/each}
	</Select.Content>
</Select.Root>
