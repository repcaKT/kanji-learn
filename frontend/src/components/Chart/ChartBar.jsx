import React from "react";
import {
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
  ResponsiveContainer,
} from "recharts";

const ChartBar = ({ progressData }) => {
  // Sample data
  console.log(progressData);

  return (
    <ResponsiveContainer width={"99%"} height={300}>
      <BarChart width={600} height={600} data={progressData}>
        <Bar dataKey="learned" fill="green" />
        {/* <CartesianGrid stroke="#ccc" /> */}
        <XAxis dataKey="name" />
        <YAxis />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default ChartBar;
