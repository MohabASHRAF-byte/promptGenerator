// src/components/PromptPage/PromptParamsAccordion.js
import React from "react";

const paramList = [
  { key: "name", label: "Prompt Name", type: "text" },
  { key: "ai_role", label: "AI Role", type: "text" },
  { key: "experience_level", label: "Experience Level", type: "select", options: ["beginner", "intermediate", "expert"] },
  { key: "code_only", label: "Code Only", type: "checkbox" },
  { key: "is_code", label: "Is Code", type: "checkbox" },
];

const PromptParamsAccordion = ({ params, onChange }) => (
  <div className="rounded-lg bg-white shadow border divide-y">
    {paramList.map(({ key, label, type, options }) => (
      <div key={key} className="p-4 flex items-center gap-4">
        <span className="font-semibold w-40">{label}:</span>
        {type === "text" && (
          <input
            className="border rounded p-2 flex-1"
            value={params[key] ?? ""}
            onChange={e => onChange(key, e.target.value)}
          />
        )}
        {type === "select" && (
          <select
            className="border rounded p-2 flex-1"
            value={params[key] ?? ""}
            onChange={e => onChange(key, e.target.value)}
          >
            {options.map(opt => (
              <option key={opt} value={opt}>{opt.charAt(0).toUpperCase() + opt.slice(1)}</option>
            ))}
          </select>
        )}
        {type === "checkbox" && (
          <input
            type="checkbox"
            checked={!!params[key]}
            onChange={e => onChange(key, e.target.checked)}
          />
        )}
      </div>
    ))}
  </div>
);

export default PromptParamsAccordion;
