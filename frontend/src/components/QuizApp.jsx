import "./QuizApp.css";
import axios from "axios";
import Header from "./Header/Header";
import Footer from "./Footer/Footer";
import Home from "./Pages/Home/Home";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Quiz from "./Pages/Quiz/Quiz";
import Result from "./Pages/Result/Result";
import { useState } from "react";
function QuizApp() {
  const [questions, setQuestions] = useState();
  const [score, setScore] = useState(0);
  const [task, setTask] = useState();

  var userID = localStorage.getItem("id");
  var userNickname = localStorage.getItem("nickname");
  const fetchQuestions = async (category = "", difficulty = "") => {
    const { data } = await axios.get(
      `http://127.0.0.1:8000/quiz/${difficulty}/${category}/${userID}`
    );

    setQuestions(data.questions);
    setTask(data.task);
  };

  return (
    <BrowserRouter>
      <div className="quizapp" style={{ backgroundImage: "url(../kanji.png)" }}>
        {/* <Header /> */}
        <Routes>
          <Route path="/" element={<Home fetchQuestions={fetchQuestions} />} />
          <Route
            path="/quiz"
            element={
              <Quiz
                name={userNickname}
                task={task}
                questions={questions}
                score={score}
                setScore={setScore}
                setQuestions={setQuestions}
              />
            }
          />
          <Route
            path="/results"
            element={
              <Result score={score} questions={questions} name={userNickname} />
            }
          />
        </Routes>
      </div>
      <Footer />
    </BrowserRouter>
  );
}

export default QuizApp;
