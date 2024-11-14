import { baseURL } from '$lib/globals';
import { createQuery } from '@tanstack/svelte-query';
import axios from 'axios';

export const load = () => {
	return {
		sources: createQuery({
			queryKey: ['sources'],
			queryFn: () => axios.get(`${baseURL}/sources/`)
		})
	};
};
