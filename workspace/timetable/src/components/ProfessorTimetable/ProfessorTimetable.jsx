import "./ProfessorTimetable.css";
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function ProfessorTimetable() {
  const [timetableData, setTimetableData] = useState([]);
  const [professorName, setProfessorName] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5001/api/lecture_list")
      .then((response) => {
        setTimetableData(response.data);
      })
      .catch((error) => {
        console.log("Error fetching timetable data : ", error);
      });
  }, []); // 빈 배열을 넣어서 컴포넌트가 마운트될 때 한 번만 실행되게 함.

  const sortByStartTime = (data) => {
    return data.slice().sort((a, b) => {
      const startTimeA = new Date(`1970-01-01T${a.l_time}`);
      const startTimeB = new Date(`1970-01-01T${b.l_time}`);
      return startTimeA - startTimeB;
    });
  };

  const calculatePeriod = (startTime) => {
    const hour = parseInt(startTime.split(":")[0], 10);
    return hour - 8; // 1교시는 9시부터 시작
  };

  const filterByProfessor = (data, profName) => {
    return data.filter((lecture) => lecture.p_name === profName);
  };

  const handleInputChange = (event) => {
    setProfessorName(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 입력받은 교수 이름으로 시간표 데이터 필터링
    const filteredData = filterByProfessor(timetableData, professorName);
    setTimetableData(filteredData);
  };

  return (
    <div className="Timetable">
      <h1>교수 시간표</h1>
      <form onSubmit={handleSubmit}>
        <label>
          교수 성함:
          <input
            type="text"
            value={professorName}
            onChange={handleInputChange}
          />
        </label>
        <button type="submit">검색</button>
      </form>
      <table border="1">
        <thead>
          <tr>
            <th></th>
            <th>월요일</th>
            <th>화요일</th>
            <th>수요일</th>
            <th>목요일</th>
            <th>금요일</th>
          </tr>
        </thead>
        <tbody>
          {[1, 2, 3, 4, 5, 6, 7].map((period) => (
            <tr key={period}>
              <th>{period}교시</th>
              {["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].map(
                (day) => {
                  // 해당 요일의 시간표 데이터를 시작 시간을 기준으로 정렬
                  const sortedData = sortByStartTime(
                    timetableData.filter(
                      (item) =>
                        item.l_day === day && item.p_name === professorName
                    )
                  );
                  return (
                    <td key={day}>
                      {sortedData.map((lecture, index) => {
                        const startTime = calculatePeriod(lecture.l_time);
                        const endTime = calculatePeriod(lecture.end_time);
                        // 해당 과목이 현재 교시에 포함되는지 확인
                        if (startTime <= period && period < endTime) {
                          return (
                            <div key={`${day}-${period}-${index}`}>
                              {lecture.c_name}
                              <br />[{lecture.p_name}]
                            </div>
                          );
                        }
                        return null;
                      })}
                    </td>
                  );
                }
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
