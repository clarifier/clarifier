import { baseURL } from '$lib/globals';
import { createQuery } from '@tanstack/svelte-query';
import axios from 'axios';

export const sourceQuery = (id: string) =>
	createQuery({
		queryKey: ['source', id],
		queryFn: () => axios.get(`${baseURL}/sources/${id}/`)
	});
