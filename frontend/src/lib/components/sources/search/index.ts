import File from './File.svelte';
import OpenML from './OpenML.svelte';
import PostgreSQL from './PostgreSQL.svelte';
import TfDS from './TFDS.svelte';
import Url from './URL.svelte';
import Kaggle from './Kaggle.svelte';

export { File, OpenML, PostgreSQL, TfDS, Url, Kaggle };

export const sources = {
	upload: { label: 'Upload a file (.csv, .parquet)', component: File },
	url: { label: 'Download from URL', component: Url },
	postgresql: { label: 'Connect a PostgreSQL table', component: PostgreSQL },
	openml: { label: 'Search an OpenML dataset', component: OpenML },
	tfds: { label: 'Search TensorFlow datasets', component: TfDS },
	kaggle: { label: 'Search Kaggle datasets', component: Kaggle }
} as const;
