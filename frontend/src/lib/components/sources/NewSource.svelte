<script lang="ts">
	type Source = {
		id: String;
		name: String;
		description: String;
		size: String;
		type: String;
		source: String;
	};

	import * as Card from '$lib/components/ui/card';
	import { PlusCircle } from 'lucide-svelte';
</script>

<a href="/source/new" class="group">
	<Card.Root
		class="flex h-full w-full flex-col items-center justify-center group-hover:border-primary group-hover:shadow-md"
	>
		<Card.Content class="m-0 flex flex-col items-center justify-center gap-2 p-0">
			<h1 class="text-lg font-semibold">New Source</h1>
			<PlusCircle />
		</Card.Content>
	</Card.Root>
</a>
