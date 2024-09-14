import { CloudDownload, Database, FileUp } from 'lucide-svelte';
import type { ComponentType } from 'svelte';
import type { Icon } from 'lucide-svelte';

type SourceTypes = {
	[page: string]: {
		icon: ComponentType<Icon>;
		title: string;
		description: string;
	};
};

export const sourceTypes: SourceTypes = {
	upload: { icon: FileUp, title: 'Upload file', description: 'Upload a file (.csv, .parquet)' },
	url: {
		icon: CloudDownload,
		title: 'Download file from URL',
		description: 'Download a file directly from URL'
	},
	//	postgresql: { icon: Database, title: 'PostgreSQL', description: 'Connect to a PostgreSQL table' },
	openml: { icon: CloudDownload, title: 'OpenML', description: 'Search OpenML datasets' }
	//	tfds: { icon: CloudDownload, title: 'TensorFlow', description: 'Search TensorFlow datasets' },
	//	kaggle: { icon: CloudDownload, title: 'Kaggle', description: 'Search Kaggle datasets' }
} as const;
