import React from "react";
import { useParams } from "react-router-dom";
import PromptDetails from "../components/PromptPage/PromptDetails";

const Prompt = () => {
  const { id } = useParams();
  return <PromptDetails promptId={id} />;
};

export default Prompt;
