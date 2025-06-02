import api from "./index";

export const addInstruction = (data) => api.post("/instruction", data);
export const updateInstruction = (id, data) => api.put(`/instruction/${id}`, data);
export const deleteInstruction = (ids) => api.delete("/instruction", { data: ids });
