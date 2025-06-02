import React, { useEffect, useState } from "react";
import { getPrompts, addPrompt } from "../../api/prompts";
import PromptItem from "./PromptItem";

const MainContent = ({ projectId, onPromptClick }) => {
  const [prompts, setPrompts] = useState([]);
  const [showAdd, setShowAdd] = useState(false);
  const [newName, setNewName] = useState("");
  const [newCodeOnly, setNewCodeOnly] = useState(false);

  useEffect(() => {
    if (projectId) {
      getPrompts(projectId).then(res => setPrompts(res.data));
    }
  }, [projectId]);

  const handleAddPrompt = async () => {
    if (!newName) return;
    const res = await addPrompt({ project_id: projectId, name: newName, code_only: newCodeOnly });
    setPrompts([...prompts, res.data]);
    setShowAdd(false);
    setNewName("");
    setNewCodeOnly(false);
  };

  if (!projectId) return <div className="main-content">Select a project</div>;

  return (
    <div className="main-content">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2>Prompts</h2>
        <button className="add-project-btn" onClick={() => setShowAdd(!showAdd)}>
          + Add Prompt
        </button>
      </div>
      {showAdd && (
        <div className="add-project-form" style={{ marginBottom: 16 }}>
          <input
            placeholder="Prompt Name"
            value={newName}
            onChange={e => setNewName(e.target.value)}
          />
          <label style={{ color: "#eee" }}>
            <input
              type="checkbox"
              checked={newCodeOnly}
              onChange={e => setNewCodeOnly(e.target.checked)}
            />{" "}
            Code Only
          </label>
          <div>
            <button onClick={handleAddPrompt}>Add</button>
            <button onClick={() => setShowAdd(false)}>Cancel</button>
          </div>
        </div>
      )}
      <div className="prompt-list">
        {prompts.map(p => (
          <PromptItem key={p.id} prompt={p} onClick={() => onPromptClick(p.id)} />
        ))}
      </div>
    </div>
  );
};

export default MainContent;
