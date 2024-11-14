export type Source = {
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
