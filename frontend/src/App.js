import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import Sidebar from "./components/Sidebar/Sidebar";
import Home from "./pages/Home";
import Prompt from "./pages/Prompt";
import "./theme.css";

const App = () => {
  const [selectedProject, setSelectedProject] = useState(null);
  const navigate = useNavigate();

  const handlePromptClick = (id) => navigate(`/prompt/${id}`);

  return (
    <div className="app dark-mode">
      <Sidebar selectedProjectId={selectedProject} onSelect={setSelectedProject} />
      <div className="main-area">
        <Routes>
          <Route path="/" element={<Home projectId={selectedProject} onPromptClick={handlePromptClick} />} />
          <Route path="/prompt/:id" element={<Prompt />} />
        </Routes>
      </div>
    </div>
  );
};

const AppWithRouter = () => (
  <Router>
    <App />
  </Router>
);

export default AppWithRouter;
