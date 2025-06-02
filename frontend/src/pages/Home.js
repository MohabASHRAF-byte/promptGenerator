import React from "react";
import MainContent from "../components/Main/MainContent";

const Home = ({ projectId, onPromptClick }) => (
  <MainContent projectId={projectId} onPromptClick={onPromptClick} />
);

export default Home;
