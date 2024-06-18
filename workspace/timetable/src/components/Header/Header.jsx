import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

export default function Header() {
  return (
    <div className="header">
      <Link to="/student_table">학생 테이블</Link>
      <Link to="/professor_table">교수 테이블</Link>
    </div>
  );
}
