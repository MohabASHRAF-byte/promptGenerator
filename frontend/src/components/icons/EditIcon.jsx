import React from "react";

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

export default EditIcon;
