<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { cn } from '$lib/utils';
	import { AlertCircle, CircleCheck, Hourglass, Loader, Loader2 } from 'lucide-svelte';
	import { Badge } from '../ui/badge';
	import type { Source } from '$lib/types/source';

	interface Props {
		source: Source;
	}

	let { source }: Props = $props();
	const { id, name, description, source: src } = source;
	const status = source.data?.status;

	const statusIcons = {
		fetching: Loader2,
		working: Loader2,
		queued: Hourglass,
		success: CircleCheck,
		failed: AlertCircle
	};
	const StatusIcon = statusIcons[status ?? 'queued'];
</script>

<a href={`/source/${id}`} class="group transition">
	<Card.Root
		class={cn([
			'flex h-full w-full flex-col justify-between group-hover:!border-primary group-hover:shadow-md',
			(status == 'fetching' || status == 'working') && 'blue-border-animate',
			status == 'queued' && 'orange-border-animate',
			status == 'failed' && 'border-red-400'
		])}
	>
		<Card.Header>
			<Card.Title>{name}</Card.Title>
			<Card.Description class="h-16 truncate text-wrap">{description}</Card.Description>
		</Card.Header>
		<Card.Footer class="flex flex-row flex-wrap gap-1 font-mono text-xs">
			<Badge variant="outline" title={src}><span class="max-w-[5em] truncate">{src}</span></Badge>
			<StatusIcon class="ml-auto" size={16} />
		</Card.Footer>
	</Card.Root>
</a>

<style lang="postcss">
	:global(.blue-border-animate) {
		animation: blue-border-animate 5s infinite alternate;
	}

	@keyframes blue-border-animate {
		0% {
			@apply border-blue-400 shadow-blue-400;
		}
		100% {
			@apply border-blue-500 shadow-blue-500;
		}
	}

	:global(.orange-border-animate) {
		animation: orange-border-animate 5s infinite alternate;
	}

	@keyframes orange-border-animate {
		0% {
			@apply border-orange-400 shadow-orange-400;
		}
		100% {
			@apply border-orange-500 shadow-orange-500;
		}
	}
</style>
