// src/components/PromptPage/PromptOutput.js
import React, { useEffect } from "react";
import useDebounce from "../hooks/useDebounce";

const PromptOutput = ({
  promptId,
  params,
  input,
  output,
  setOutput,
  loading,
  setLoading,
}) => {
  const debouncedInput = useDebounce(input, 500);

  useEffect(() => {
    if (!debouncedInput || !promptId) return;

    setLoading(true);
    fetch(`/api/prompts/${promptId}/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: debouncedInput }),
    })
      .then(res => res.json())
      .then(data => setOutput(data.prompt))
      .catch(() => setOutput("Error generating prompt."))
      .finally(() => setLoading(false));
  }, [debouncedInput, promptId, setOutput, setLoading]);

  return (
    <div className="h-full">
      <h2 className="font-bold text-xl mb-4">Generated Prompt:</h2>
      <div className="border rounded-lg bg-gray-50 p-4 min-h-[200px] max-h-[60vh] overflow-y-auto text-base whitespace-pre-wrap">
        {loading ? <span className="animate-pulse">Generating...</span> : output}
      </div>
    </div>
  );
};

export default PromptOutput;
