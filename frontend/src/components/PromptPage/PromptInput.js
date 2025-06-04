// src/components/PromptPage/PromptInput.js
import React from "react";

const PromptInput = ({ input, onInputChange }) => (
  <div>
    <label className="block mb-2 font-bold text-lg">Prompt Input:</label>
    <textarea
      className="w-full min-h-[120px] p-3 border rounded resize-y focus:outline-none focus:ring-2"
      value={input}
      onChange={e => onInputChange(e.target.value)}
      placeholder="Type your prompt here..."
    />
  </div>
);

export default PromptInput;
