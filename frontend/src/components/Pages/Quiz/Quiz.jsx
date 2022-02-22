import React, { useEffect, useState } from "react";

const Quiz = ({ name, questions, score, setScore, setQuestions }) => {
  const [options, setOptions] = useState();
  const [currQues, setCurrQues] = useState(0);

  useEffect(() => {
    console.log(questions);
  }, [questions]);
  return <div>QuizPage</div>;
};

export default Quiz;
