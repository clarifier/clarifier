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
	import { Badge } from '../ui/badge';

	export let source: Source;
	const { id, name, description, size, type, source: src } = source;
</script>

<a href={`/source/${id}`} class="group transition">
	<Card.Root
		class="flex h-full w-full flex-col justify-between group-hover:border-primary group-hover:shadow-md"
	>
		<Card.Header>
			<Card.Title>{name}</Card.Title>
			<Card.Description class="h-16 truncate text-wrap">{description}</Card.Description>
		</Card.Header>
		<Card.Footer class="flex flex-row flex-wrap gap-1 font-mono text-xs">
			<Badge variant="outline" title={size}>{size}</Badge>
			<Badge variant="outline" title={src}><span class="max-w-[5em] truncate">{src}</span></Badge>
			<Badge variant="outline" title={type}>{type}</Badge>
		</Card.Footer>
	</Card.Root>
</a>
