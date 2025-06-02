import React from "react";

const ProjectItem = ({ project, selected, onClick }) => (
  <div
    className={`project-item${selected ? " selected" : ""}`}
    onClick={onClick}
  >
    {project.name}
  </div>
);

export default ProjectItem;
