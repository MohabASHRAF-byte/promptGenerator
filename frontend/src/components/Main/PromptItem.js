import React from "react";

const PromptItem = ({ prompt, onClick }) => (
  <div className="prompt-item" onClick={onClick}>
    {prompt.name}
  </div>
);

export default PromptItem;
