import React from "react";

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

export default CopyIcon;
