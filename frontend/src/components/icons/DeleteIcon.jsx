import React from "react";

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

export default DeleteIcon;
