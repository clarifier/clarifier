import { baseURL } from '$lib/globals';
import axios from 'axios';

export type KaggleSource = {
	id: string;
	documentType: string;
	databaseId: number;
	title: string;
	url: string;
	thumbnailImageUrl: string;
	rank: number;
	votes: number;
	date: string;
	authorSlug: string;
	datasetInfo: {
		size: number;
		fileTypes: string[];
		currentDatasetVersionId: number;
		datasetSlug: string;
		totalDownloads: number;
		subtitle?: string;
	};
	authorDisplayName: string;
	matchedText?: string;
};

export type SearchResponse = {
	documents: KaggleSource[];
};

export const searchKaggle = (search: string) =>
	axios.post<SearchResponse>('https://www.kaggle.com/api/i/search.SearchWebService/FullSearchWeb', {
		query: `${search} in:datasets`,
		page: 1,
		resultsPerPage: 20,
		showPrivate: true
	});

export const addKaggleSource = async (source: KaggleSource) => {
	return axios.post(`${baseURL}/sources/upload/kaggle`, {
		id: source.id
	});
};

export default { searchKaggle, addKaggleSource };
