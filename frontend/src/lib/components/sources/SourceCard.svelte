<script lang="ts">
	type Source = {
		id: string;
		name: string;
		description: string;
		size: string;
		type: string;
		source: string;
		data?: {
			status: 'fetching' | 'success' | 'failed' | 'working' | 'queued';
			ch_table?: string;
		};
	};

	import * as Card from '$lib/components/ui/card';
	import { cn } from '$lib/utils';
	import { Badge } from '../ui/badge';

	interface Props {
		source: Source;
	}

	let { source }: Props = $props();
	const { id, name, description, size, type, source: src } = source;
	const status = source.data?.status;
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
