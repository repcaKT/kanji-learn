import React, { useEffect, useState, useContext } from "react";
import Register from "./components/Register";
import Login from "./components/Login";
import Header from "./components/Header";
import { UserContext } from "./context/UserContext";
import QuizApp from "./components/QuizApp";
const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);
  const progressdata = [
    { name: "N5", learned: 100 },
    { name: "N4", learned: 70 },
    { name: "N3", learned: 40 },
    { name: "N2", learned: 20 },
    { name: "N1", learned: 2 },
  ];
  const [progressData, setProgressData] = useState(progressdata);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
  };
  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <>
      <Header title={message} />
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {!token ? (
            <div className="columns">
              <Login /> <Register />
            </div>
          ) : (
            <QuizApp
              progressData={progressData}
              setProgressData={setProgressData}
            />
          )}
        </div>
        <div className="column"></div>
      </div>
    </>
  );
};

export default App;
