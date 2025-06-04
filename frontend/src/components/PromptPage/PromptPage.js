// src/components/PromptPage/PromptPage.js
import React, { useState, useEffect } from "react";
import PromptParamsAccordion from "./PromptParamsAccordion";
import PromptInput from "./PromptInput";
import PromptOutput from "./PromptOutput";

const PromptPage = ({ promptId }) => {
  const [params, setParams] = useState(null);
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  // Fetch prompt data on mount
  useEffect(() => {
    fetch(`/api/prompts/${promptId}`)
      .then(res => res.json())
      .then(data => setParams(data));
  }, [promptId]);

  // Handler for updating any prompt parameter
  const handleParamChange = (key, value) => {
    setParams(prev => ({ ...prev, [key]: value }));
    // Optionally, send update to server
    fetch(`/api/prompts/${promptId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ [key]: value }),
    });
  };

  // Handler for prompt input change
  const handleInputChange = val => setInput(val);

  return (
    <div className="flex h-[90vh] border rounded-xl shadow-lg overflow-hidden bg-white">
      <div className="w-1/2 p-6 border-r flex flex-col gap-6 bg-gray-50">
        {params && (
          <PromptParamsAccordion params={params} onChange={handleParamChange} />
        )}
        <PromptInput input={input} onInputChange={handleInputChange} />
      </div>
      <div className="w-1/2 p-6 bg-white">
        <PromptOutput
          promptId={promptId}
          params={params}
          input={input}
          output={output}
          setOutput={setOutput}
          loading={loading}
          setLoading={setLoading}
        />
      </div>
    </div>
  );
};

export default PromptPage;
