import React, { useEffect, useState } from "react";
import { getPrompt, updatePrompt, generatePrompt } from "../../api/prompts";
import {
  updateInstruction,
  deleteInstruction,
  addInstruction,
} from "../../api/instructions";

const CopyIcon = ({ onClick }) => (
  <svg
    onClick={onClick}
    width="20"
    height="20"
    viewBox="0 0 24 24"
    fill="#a259e6"
    style={{ cursor: "pointer", marginLeft: 8, verticalAlign: "middle" }}
  >
    <rect
      x="9"
      y="9"
      width="13"
      height="13"
      rx="2"
      fill="none"
      stroke="#a259e6"
      strokeWidth="2"
    />
    <rect
      x="3"
      y="3"
      width="13"
      height="13"
      rx="2"
      fill="none"
      stroke="#a259e6"
      strokeWidth="2"
    />
  </svg>
);

const EditIcon = ({ onClick }) => (
  <svg
    onClick={onClick}
    width="20"
    height="20"
    viewBox="0 0 24 24"
    fill="none"
    style={{ cursor: "pointer", marginLeft: 12, verticalAlign: "middle" }}
  >
    <path
      d="M5 20h14M16.5 3.5a2.121 2.121 0 113 3L7 19.5 3 21l1.5-4L16.5 3.5z"
      stroke="#38b000"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

const DeleteIcon = ({ onClick }) => (
  <svg
    onClick={onClick}
    width="20"
    height="20"
    viewBox="0 0 24 24"
    fill="none"
    style={{ cursor: "pointer", marginLeft: 8, verticalAlign: "middle" }}
  >
    <path
      d="M3 6h18M8 6V4a2 2 0 012-2h4a2 2 0 012 2v2M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6h14z"
      stroke="#e34d4d"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <line x1="10" y1="11" x2="10" y2="17" stroke="#e34d4d" strokeWidth="2" />
    <line x1="14" y1="11" x2="14" y2="17" stroke="#e34d4d" strokeWidth="2" />
  </svg>
);

const PromptDetails = ({ promptId }) => {
  const [prompt, setPrompt] = useState(null);
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);
  const [editing, setEditing] = useState(null);
  const [newInstruction, setNewInstruction] = useState("");
  const [saving, setSaving] = useState(false);
  const [copied, setCopied] = useState(false);

  const fetchPrompt = async () => {
    const res = await getPrompt(promptId);
    setPrompt(res.data);
  };

  useEffect(() => {
    fetchPrompt();
    // eslint-disable-next-line
  }, [promptId]);

  // Generate prompt
  const handleGenerate = async () => {
    setSaving(true);
    const res = await generatePrompt(promptId, { content: input });
    setResult(res.data.prompt);
    setSaving(false);
  };

  // Parameter handlers
  const handleParamChange = async (field, value) => {
    setPrompt((prev) => ({ ...prev, [field]: value }));
    await updatePrompt(promptId, { [field]: value });
  };

  // Edit instruction
  const handleEditInstruction = async (id, content) => {
    await updateInstruction(id, { content });
    setEditing(null);
    fetchPrompt();
  };

  // Delete instruction
  const handleDeleteInstruction = async (id) => {
    await deleteInstruction([id]);
    fetchPrompt();
  };

  // Add instruction
  const handleAddInstruction = async () => {
    if (!newInstruction) return;
    await addInstruction({
      promptId: promptId,
      content: newInstruction,
      CheckGrammarAndSpelling: false,
    });
    setNewInstruction("");
    fetchPrompt();
  };

  // Copy output with animation
  const handleCopy = () => {
    if (result) {
      navigator.clipboard.writeText(result);
      setCopied(true);
      setTimeout(() => setCopied(false), 1200);
    }
  };

  if (!prompt)
    return <div className="prompt-details dark-panel">Loading...</div>;

  return (
    <div className="prompt-details dark-panel">
      {/* Title */}
      <h1 className="prompt-title">{prompt.name}</h1>

      {/* All prompt parameters */}
      <div className="parameters-section" style={{ marginBottom: 24 }}>
        <div className="row-center" style={{ marginBottom: 10 }}>
          <label className="toggle-label" style={{ marginRight: 24 }}>
            <input
              type="checkbox"
              checked={prompt.code_only}
              onChange={e => handleParamChange("code_only", e.target.checked)}
            />
            <span className="toggle-slider"></span>
            <span style={{ marginLeft: 8 }}>Code Only</span>
          </label>
          <label className="toggle-label" style={{ marginRight: 24 }}>
            <input
              type="checkbox"
              checked={prompt.is_code}
              onChange={e => handleParamChange("is_code", e.target.checked)}
            />
            <span className="toggle-slider"></span>
            <span style={{ marginLeft: 8 }}>Is Code</span>
          </label>
        </div>
        <div className="row-center" style={{ marginBottom: 10 }}>
          <label style={{ marginRight: 8, minWidth: 90 }}>AI Role:</label>
          <input
            type="text"
            value={prompt.ai_role || ""}
            onChange={e => handleParamChange("ai_role", e.target.value)}
            className="param-input"
            style={{ minWidth: 180 }}
            placeholder="e.g. assistant"
          />
        </div>
        <div className="row-center" style={{ marginBottom: 10 }}>
          <label style={{ marginRight: 8, minWidth: 90 }}>Experience:</label>
          <input
            type="text"
            value={prompt.experience_level || ""}
            onChange={e => handleParamChange("experience_level", e.target.value)}
            className="param-input"
            style={{ minWidth: 180 }}
            placeholder="e.g. expert"
          />
        </div>
      </div>

      {/* Instructions */}
      <div className="instructions-section">
        <h3>Instructions</h3>
        <ul className="instructions-list">
          {prompt.instructions.map((ins, idx) => (
            <li key={ins.id} className="instruction-item">
              <span className="bullet">{idx + 1}.</span>
              {editing && editing.id === ins.id ? (
                <>
                  <input
                    className="edit-input"
                    value={editing.content}
                    onChange={e => setEditing({ ...editing, content: e.target.value })}
                    autoFocus
                  />
                  <button
                    className="btn save"
                    onClick={() => handleEditInstruction(ins.id, editing.content)}
                  >
                    Save
                  </button>
                  <button
                    className="btn cancel"
                    onClick={() => setEditing(null)}
                  >
                    Cancel
                  </button>
                </>
              ) : (
                <>
                  <span style={{ flex: 1 }}>{ins.content}</span>
                  <EditIcon
                    onClick={() => setEditing({ id: ins.id, content: ins.content })}
                  />
                  <DeleteIcon onClick={() => handleDeleteInstruction(ins.id)} />
                </>
              )}
            </li>
          ))}
        </ul>
        {/* Add new instruction */}
        <div className="add-instruction-row">
          <input
            className="add-input"
            placeholder="New instruction..."
            value={newInstruction}
            onChange={e => setNewInstruction(e.target.value)}
            onKeyDown={e => {
              if (e.key === "Enter") handleAddInstruction();
            }}
          />
          <button className="btn add" onClick={handleAddInstruction}>
            Add
          </button>
        </div>
      </div>

      {/* Generation Section */}
      <div className="generation-section-split">
        {/* Left: Input */}
        <div className="generation-input-box">
          <h3>Input Query</h3>
          <textarea
            value={input}
            onChange={e => setInput(e.target.value)}
            placeholder="Enter input for prompt generation..."
          />
          <button
            className="btn main"
            onClick={handleGenerate}
            disabled={saving}
          >
            {saving ? "Generating..." : "Generate"}
          </button>
        </div>
        {/* Right: Output */}
        <div className="generation-output-box">
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
            }}
          >
            <h3>Output</h3>
            {result && (
              <span style={{ display: "flex", alignItems: "center" }}>
                <CopyIcon onClick={handleCopy} />
                <span
                  style={{
                    marginLeft: 8,
                    color: "#38b000",
                    opacity: copied ? 1 : 0,
                    transition: "opacity 0.5s",
                    fontWeight: "bold",
                    fontSize: 14,
                    verticalAlign: "middle",
                  }}
                >
                  Copied!
                </span>
              </span>
            )}
          </div>
          <div className="output-area">
            <pre style={{ whiteSpace: "pre-wrap", wordBreak: "break-word" }}>
              {result || "—"}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PromptDetails;
