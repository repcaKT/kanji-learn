import { Button } from "@material-ui/core";
import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import "./Result.css";
import ResultTable from "./ResultTable";

const Result = ({ score, questions, name, setScore, setProgressData }) => {
  const history = useNavigate();
  var userID = localStorage.getItem("id");

  const submitResults = async () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers_selected: questions, user_id: userID }),
    };
    const response = await fetch("/api/currentprogress", requestOptions);
    const data = await response.json();
    if (response.ok) {
      setProgressData(data.progress);
      setScore(0);
      history("/");
    } else {
      // localStorage.setItem("test", data.test);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    submitResults();
  };
  console.log(questions);
  return (
    <div className="result">
      <span className="title">Correct answers: {score}</span>
      <form onSubmit={handleSubmit}>
        <Button
          variant="contained"
          color="secondary"
          size="large"
          style={{ alignSelf: "center", marginTop: 20 }}
          type="submit"
          // href="/"
        >
          Save results and return
        </Button>
      </form>
      <br></br>
      <ResultTable questions={questions}></ResultTable>
    </div>
  );
};

export default Result;
