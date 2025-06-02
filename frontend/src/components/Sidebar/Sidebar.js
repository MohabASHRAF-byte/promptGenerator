import React, { useEffect, useState } from "react";
import { getProjects } from "../../api/projects";
import ProjectItem from "./ProjectItem";
import AddProject from "./AddProject";

const Sidebar = ({ selectedProjectId, onSelect }) => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then(res => setProjects(res.data));
  }, []);

  const handleAdd = (newProj) => setProjects([...projects, newProj]);

  return (
    <aside className="sidebar">
      <div className="sidebar-header">Projects</div>
      <div className="project-list">
        {projects.map((p) => (
          <ProjectItem
            key={p.id}
            project={p}
            selected={selectedProjectId === p.id}
            onClick={() => onSelect(p.id)}
          />
        ))}
        <AddProject onAdd={handleAdd} />
      </div>
    </aside>
  );
};

export default Sidebar;
