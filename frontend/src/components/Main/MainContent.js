import React, { useEffect, useState } from "react";
import { getPrompts } from "../../api/prompts";
import PromptItem from "./PromptItem";

const MainContent = ({ projectId, onPromptClick }) => {
  const [prompts, setPrompts] = useState([]);

  useEffect(() => {
    if (projectId) {
      getPrompts(projectId).then(res => setPrompts(res.data));
    }
  }, [projectId]);

  if (!projectId) return <div className="main-content">Select a project</div>;

  return (
    <div className="main-content">
      <div className="prompt-list">
        {prompts.map(p => (
          <PromptItem key={p.id} prompt={p} onClick={() => onPromptClick(p.id)} />
        ))}
      </div>
    </div>
  );
};

export default MainContent;
