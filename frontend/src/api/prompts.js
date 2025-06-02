import api from "./index";

export const getPrompts = (projectId) => api.get("/prompts", { params: { projectId } });
export const getPrompt = (id) => api.get(`/prompts/${id}`);
export const addPrompt = (data) => api.post("/prompts", data);
export const updatePrompt = (id, data) => api.put(`/prompts/${id}`, data);
export const deletePrompt = (id) => api.delete(`/prompts/${id}`);
export const generatePrompt = (id, data) => api.post(`/prompts/${id}/generate`, data);
