import { Button } from "@material-ui/core";
import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Result = ({ score, questions, name }) => {
  const history = useNavigate();

  useEffect(() => {
    if (!questions) {
      history("/");
    }
  }, [questions, history]);

  return (
    <div classname="result">
      <span className="title">Results: {score}</span>
      <Button></Button>
    </div>
  );
};

export default Result;
