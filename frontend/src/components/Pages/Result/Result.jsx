import { Button } from "@material-ui/core";
import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import "./Result.css";

const Result = ({ score, questions, name }) => {
  const history = useNavigate();

  // useEffect(() => {
  //   if (!questions) {
  //     history("/");
  //   }
  // }, [questions, history]);

  return (
    <div className="result">
      <span className="title">Correct answers: {score}</span>
      <Button
        variant="contained"
        color="secondary"
        size="large"
        style={{ alignSelf: "center", marginTop: 20 }}
        href="/"
      >
        Save results and return
      </Button>
    </div>
  );
};

export default Result;
