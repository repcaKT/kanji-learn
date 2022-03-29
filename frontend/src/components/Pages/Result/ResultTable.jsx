import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import "./ResultTable.css";
const ResultTable = ({ questions }) => {
  function createData(number, item, qty, price) {
    return { number, item, qty, price };
  }

  const color = ["wrongSelected", "correctSelected"];
  const rows = [
    createData(1, "Apple", 5, 3),
    createData(2, "Orange", 2, 2),
    createData(3, "Grapes", 3, 1),
    createData(4, "Tomato", 2, 1.6),
    createData(5, "Mango", 1.5, 4),
  ];
  //   console.log(questions[0]);
  return (
    <TableContainer component={Paper}>
      <Table class="tablica" aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Kanji</TableCell>
            <TableCell align="right">Reading</TableCell>
            <TableCell align="right">Translation</TableCell>
            <TableCell align="right">Selected answer</TableCell>
            <TableCell align="right">Correct answer</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {questions.map((row) => (
            <TableRow key={row.number} className={color[row.correct]}>
              <TableCell component="th" scope="row">
                {row.kanji}
              </TableCell>
              <TableCell align="right">{row.reading}</TableCell>
              <TableCell align="right">{row.translation}</TableCell>
              <TableCell align="right">{row.selected_question}</TableCell>
              <TableCell align="right">{row.correct_answer}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ResultTable;
