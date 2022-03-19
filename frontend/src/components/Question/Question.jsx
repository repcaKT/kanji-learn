import { Button } from "@material-ui/core";
import React from "react";
import { useState } from "react";
import ErrorMessage from "../ErrorMessage";
import { useNavigate } from "react-router-dom";
import "./Question.css";
const Question = ({
  currQues,
  setCurrQues,
  questions,
  task,
  question,
  options,
  correct,
  score,
  setScore,
  setQuestions,
}) => {
  const [selected, setSelected] = useState();
  const [error, setError] = useState(false);

  const handleSelect = (i) => {
    if (selected === i && selected === correct) return "selected";
    else if (selected === i && selected !== correct) return "wrong";
    else if (i === correct) return "selected";
  };

  const handleCheck = (i) => {
    setSelected(i);
    if (i === correct) setScore(score + 1);
    setError(false);
  };

  const history = useNavigate();

  const handleNext = () => {
    if (currQues > 8) {
      history("/results");
    } else if (selected) {
      setCurrQues(currQues + 1);
      setSelected();
    } else {
      setError("Please select an answer");
    }
  };

  const handleQuit = () => {};

  const kanjiQuestionNumber = {
    0: "一 (いち)",
    1: "二 (に)",
    2: "三 (さん)",
    3: "四 (よん)",
    4: "五 (ご)",
    5: "六 (ろく)",
    6: "七 (なな)",
    7: "八 (はち)",
    8: "九 (きゅ)",
    9: "十 (じゅう)",
  };

  return (
    <div className="question">
      <h1>質問: {kanjiQuestionNumber[currQues]}</h1>

      <div className="singleQuestion">
        <h2>{task}</h2>
        <h2>{question}</h2>
        {error && <ErrorMessage>{error}</ErrorMessage>}
        <div className="options">
          {options &&
            options.map((i) => (
              <button
                onClick={() => handleCheck(i)}
                className={`singleOption ${selected && handleSelect(i)}`}
                key={i}
                disabled={selected}
              >
                {i}
              </button>
            ))}
        </div>
        <div className="controls">
          <Button
            variant="contained"
            color="secondary"
            size="large"
            style={{ width: 185 }}
            href="/"
            onClick={handleQuit}
          >
            Quit
          </Button>
          <Button
            variant="contained"
            color="primary"
            size="large"
            style={{ width: 185 }}
            onClick={handleNext}
          >
            Next
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Question;
