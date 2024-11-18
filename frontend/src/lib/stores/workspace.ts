import { writable } from 'svelte/store';

export const workspace = writable({ value: 'default', label: 'Default Workspace' });
