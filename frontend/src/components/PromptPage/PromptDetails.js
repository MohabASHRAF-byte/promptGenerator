import React, { useEffect, useState } from "react";
import { getPrompt, generatePrompt } from "../../api/prompts";

const PromptDetails = ({ promptId }) => {
  const [prompt, setPrompt] = useState(null);
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);

  useEffect(() => {
    getPrompt(promptId).then(res => setPrompt(res.data));
  }, [promptId]);

  const handleGenerate = async () => {
    const res = await generatePrompt(promptId, { content: input });
    setResult(res.data.prompt);
  };

  if (!prompt) return <div>Loading...</div>;

  return (
    <div className="prompt-details">
      <h2>{prompt.name}</h2>
      <pre>{JSON.stringify(prompt, null, 2)}</pre>
      <div className="generate-section">
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Enter input for prompt generation..."
        />
        <button onClick={handleGenerate}>Generate</button>
      </div>
      {result && (
        <div className="generation-result">
          <strong>Result:</strong>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
};

export default PromptDetails;
