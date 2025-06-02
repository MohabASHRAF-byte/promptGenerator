import React, { useState } from "react";
import { addProject } from "../../api/projects";

const AddProject = ({ onAdd }) => {
  const [show, setShow] = useState(false);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleAdd = async () => {
    if (!name) return;
    const res = await addProject({ name, description });
    onAdd(res.data);
    setShow(false);
    setName("");
    setDescription("");
  };

  return show ? (
    <div className="add-project-form">
      <input
        placeholder="Project Name"
        value={name}
        onChange={e => setName(e.target.value)}
      />
      <input
        placeholder="Description"
        value={description}
        onChange={e => setDescription(e.target.value)}
      />
      <button onClick={handleAdd}>Add</button>
      <button onClick={() => setShow(false)}>Cancel</button>
    </div>
  ) : (
    <button className="add-project-btn" onClick={() => setShow(true)}>
      + Add Project
    </button>
  );
};

export default AddProject;
