import "./QuizApp.css";
import Header from "./Header/Header";
import Footer from "./Footer/Footer";
import Home from "./Pages/Home/Home";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Quiz from "./Pages/Quiz/Quiz";
import Result from "./Pages/Result/Result";
function QuizApp() {
  const fetchQuestions = () => {};

  return (
    <BrowserRouter>
      <div className="quizapp" style={{ backgroundImage: "url(../kanji.png)" }}>
        {/* <Header /> */}
        <Routes>
          <Route path="/" element={<Home fetchQuestions={fetchQuestions} />} />
          <Route path="/quiz" element={<Quiz />} />
          <Route path="/result" element={<Result />} />
        </Routes>
      </div>
      <Footer />
    </BrowserRouter>
  );
}

export default QuizApp;
