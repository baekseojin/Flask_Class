import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import StudentTimetable from "./components/StudentTimetable/StudentTimetable";
import ProfessorTimetable from "./components/ProfessorTimetable/ProfessorTimetable";

function App() {
  return (
    <div className="App">
      <StudentTimetable />
      <ProfessorTimetable />
    </div>
  );
}

export default App;
