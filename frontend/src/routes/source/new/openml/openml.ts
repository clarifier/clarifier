import { baseURL } from '$lib/globals';
import axios from 'axios';

export type OpenMLSource = {
	date: string;
	reach: number;
	impact: number;
	format: string;
	description: string;
	version: number;
	nr_of_downloads: number;
	url: string;
	nr_of_likes: number;
	data_id: string;
	name: string;
	qualities: {
		NumberOfClasses: number | null;
		NumberOfMissingValues: number;
		NumberOfFeatures: number;
		NumberOfInstances: number;
	};
	runs: number;
	status: string;
};

export type SearchResponse = {
	took: number;
	timed_out: boolean;
	_shards: {
		total: number;
		successful: number;
		skipped: number;
		failed: number;
	};
	hits: {
		total: number;
		max_score: null | number;
		hits: Array<{
			_index: string;
			_type: string;
			_id: string;
			_score: null | number;
			_source: OpenMLSource;
			sort: Array<number>;
		}>;
	};
	aggregations: {
		type: {
			doc_count_error_upper_bound: number;
			sum_other_doc_count: number;
			buckets: Array<{
				key: string;
				doc_count: number;
			}>;
		};
	};
};

export const searchOpenML = (search: string) =>
	axios.post<SearchResponse>('https://www.openml.org/es/data/data/_search?type=data', {
		from: 0,
		size: 6,
		query: {
			bool: {
				must: { query_string: { query: search } },
				filter: [{ term: { status: 'active' } }],
				should: [{ term: { visibility: 'public' } }],
				minimum_should_match: 1
			}
		},
		aggs: { type: { terms: { field: '_type' } } },
		_source: [
			'data_id',
			'name',
			'version',
			'format',
			'description',
			'qualities.NumberOfInstances',
			'qualities.NumberOfFeatures',
			'qualities.NumberOfClasses',
			'qualities.NumberOfMissingValues',
			'runs',
			'nr_of_likes',
			'nr_of_downloads',
			'reach',
			'impact',
			'status',
			'date',
			'url'
		],
		sort: { runs: { order: 'desc' } }
	});

export const addOpenMLSource = async (source: OpenMLSource) => {
	return axios.post(`${baseURL}/sources/upload/openml`, {
		id: source.data_id
	});
};

export default { searchOpenML, addOpenMLSource };
