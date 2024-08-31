<script lang="ts">
	import * as Command from '$lib/components/ui/command';
	import { searchOpen } from '$lib/stores/search';
	import { onMount } from 'svelte';
	import { Badge } from '../ui/badge';

	onMount(() => {
		function handleKeydown(e: KeyboardEvent) {
			if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
				e.preventDefault();
				searchOpen.update((v) => !v);
			}
		}

		document.addEventListener('keydown', handleKeydown);

		return () => {
			document.removeEventListener('keydown', handleKeydown);
		};
	});
</script>

<Command.Dialog bind:open={$searchOpen}>
	<Command.Input placeholder="Type a command or search..." />
	<Command.List>
		<Command.Empty>No results found.</Command.Empty>
		<Command.Group heading="Suggestions">
			<Command.Item>
				Search for an OpenML dataset <Badge variant="outline" class="ml-auto">Sources</Badge>
			</Command.Item>
			<Command.Item>
				Download CSV from URL <Badge variant="outline" class="ml-auto">Sources</Badge>
			</Command.Item>
			<Command.Item>
				Open a quality dimension <Badge variant="outline" class="ml-auto">Profile</Badge>
			</Command.Item>
		</Command.Group>
	</Command.List>
</Command.Dialog>
