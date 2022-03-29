import React, { useState } from "react";
import "./Home.css";
import { Button, MenuItem, TextField } from "@material-ui/core";
import Categories from "../../../Data/Categories";
import { useNavigate } from "react-router-dom";
import ErrorMessage from "../../ErrorMessage";
import ErrorLogin from "../../ErrorLogin";
import ChartBar from "../../Chart/ChartBar";

const Home = ({ fetchQuestions, progressData }) => {
  const [category, setCategory] = useState("");
  const [difficulty, setDifficulty] = useState("");
  const [error, setError] = useState(false);
  // console.log(progressData);
  const navigate = useNavigate();

  const handleSubmit = () => {
    if (!category || !difficulty) {
      setError(true);
      return;
    } else {
      setError(false);
      fetchQuestions(category, difficulty);
      navigate("/quiz");
    }
  };

  return (
    <div className="content">
      <div className="settings">
        <span style={{ fontSize: 30 }}>Quiz Settings</span>
        <div className="settings__select">
          {error && (
            <ErrorLogin
              message={"Please choose category and difficulty"}
            ></ErrorLogin>
          )}
          {/* <TextField
            style={{ marginBottom: 25 }}
            label="Enter Your Name"
            variant="outlined"
          /> */}
          <TextField
            select
            label="Select Category"
            variant="outlined"
            style={{ marginBottom: 30 }}
            onChange={(e) => setCategory(e.target.value)}
            value={category}
          >
            {Categories.map((cat) => (
              <MenuItem key={cat.category} value={cat.value}>
                {cat.category}
              </MenuItem>
            ))}
          </TextField>

          <TextField
            select
            label="Select Difficulty"
            variant="outlined"
            style={{ marginBottom: 30 }}
            onChange={(e) => setDifficulty(e.target.value)}
            value={difficulty}
          >
            <MenuItem key="N5" value="n5">
              N5
            </MenuItem>
            <MenuItem key="N4" value="n4">
              N4
            </MenuItem>
            <MenuItem key="N3" value="n3">
              N3
            </MenuItem>
            <MenuItem key="N2" value="n2">
              N2
            </MenuItem>
            <MenuItem key="N1" value="n1">
              N1
            </MenuItem>
          </TextField>

          <Button
            variant="contained"
            color="primary"
            style={{ backgroundColor: "black", color: "#FFFFFF" }}
            size="large"
            onClick={handleSubmit}
          >
            Start learning
          </Button>
        </div>
      </div>

      <img src="/jlpt.png" className="banner" alt="learn img" />
      <ChartBar className="stats" progressData={progressData}></ChartBar>
    </div>
  );
};

export default Home;
