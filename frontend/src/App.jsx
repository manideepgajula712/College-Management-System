import { useEffect, useState } from "react";
import {
  login,
  logout,
  getStudents,
  getAttendance,
  getFaculty,
  getTimetable,
  getExaminations,
  getResults,
} from "./services/api";
import "./App.css";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [user, setUser] = useState(() => {
    const savedUser = localStorage.getItem("user");
    return savedUser ? JSON.parse(savedUser) : null;
  });

  const [students, setStudents] = useState([]);
  const [attendance, setAttendance] = useState([]);
  const [faculty, setFaculty] = useState([]);
  const [timetable, setTimetable] = useState([]);
  const [examinations, setExaminations] = useState([]);
  const [results, setResults] = useState([]);

  const [studentsLoading, setStudentsLoading] = useState(false);
  const [attendanceLoading, setAttendanceLoading] = useState(false);
  const [facultyLoading, setFacultyLoading] = useState(false);
  const [timetableLoading, setTimetableLoading] = useState(false);
  const [examinationsLoading, setExaminationsLoading] = useState(false);
  const [resultsLoading, setResultsLoading] = useState(false);

  const [attendanceError, setAttendanceError] = useState("");
  const [facultyError, setFacultyError] = useState("");
  const [timetableError, setTimetableError] = useState("");
  const [examinationsError, setExaminationsError] = useState("");
  const [resultsError, setResultsError] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();

    setError("");
    setLoading(true);

    try {
      const data = await login(username, password);

      const loggedInUser = {
        username: data.username,
        email: data.email,
        role: data.role,
      };

      localStorage.setItem(
        "user",
        JSON.stringify(loggedInUser)
      );

      setUser(loggedInUser);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!user) {
      return;
    }

    const loadDashboardData = async () => {
      /* Students */
      setStudentsLoading(true);

      try {
        const studentData = await getStudents();
        setStudents(studentData);
      } catch (error) {
        console.error(
          "Unable to load students:",
          error
        );
      } finally {
        setStudentsLoading(false);
      }

      /* Attendance */
      setAttendanceLoading(true);
      setAttendanceError("");

      try {
        const attendanceData =
          await getAttendance();

        setAttendance(attendanceData);
      } catch (error) {
        console.error(
          "Unable to load attendance:",
          error
        );

        setAttendanceError(error.message);
      } finally {
        setAttendanceLoading(false);
      }

      /* Faculty */
      setFacultyLoading(true);
      setFacultyError("");

      try {
        const facultyData = await getFaculty();

        setFaculty(facultyData);
      } catch (error) {
        console.error(
          "Unable to load faculty:",
          error
        );

        setFacultyError(error.message);
      } finally {
        setFacultyLoading(false);
      }

      /* Timetable */
      setTimetableLoading(true);
      setTimetableError("");

      try {
        const timetableData =
          await getTimetable();

        setTimetable(timetableData);
      } catch (error) {
        console.error(
          "Unable to load timetable:",
          error
        );

        setTimetableError(error.message);
      } finally {
        setTimetableLoading(false);
      }

      /* Examinations */
      setExaminationsLoading(true);
      setExaminationsError("");

      try {
        const examinationData =
          await getExaminations();

        setExaminations(examinationData);
      } catch (error) {
        console.error(
          "Unable to load examinations:",
          error
        );

        setExaminationsError(error.message);
      } finally {
        setExaminationsLoading(false);
      }

      /* Results */
      setResultsLoading(true);
      setResultsError("");

      try {
        const resultData = await getResults();

        setResults(resultData);
      } catch (error) {
        console.error(
          "Unable to load results:",
          error
        );

        setResultsError(error.message);
      } finally {
        setResultsLoading(false);
      }
    };

    loadDashboardData();
  }, [user]);

  const handleLogout = () => {
    logout();

    setUser(null);

    setStudents([]);
    setAttendance([]);
    setFaculty([]);
    setTimetable([]);
    setExaminations([]);
    setResults([]);

    setAttendanceError("");
    setFacultyError("");
    setTimetableError("");
    setExaminationsError("");
    setResultsError("");

    setUsername("");
    setPassword("");
  };

  /* LOGIN PAGE */

  if (!user) {
    return (
      <div className="login-page">
        <div className="login-card">

          <div className="login-header">
            <div className="logo">🎓</div>

            <h1>
              College Management System
            </h1>

            <p>
              Sign in to continue
            </p>
          </div>

          <form onSubmit={handleLogin}>

            <div className="form-group">
              <label>
                Username
              </label>

              <input
                type="text"
                value={username}
                onChange={(event) =>
                  setUsername(event.target.value)
                }
                placeholder="Enter username"
                required
              />
            </div>

            <div className="form-group">
              <label>
                Password
              </label>

              <input
                type="password"
                value={password}
                onChange={(event) =>
                  setPassword(event.target.value)
                }
                placeholder="Enter password"
                required
              />
            </div>

            {error && (
              <div className="error-message">
                {error}
              </div>
            )}

            <button
              type="submit"
              className="login-button"
              disabled={loading}
            >
              {loading
                ? "Signing in..."
                : "Sign In"}
            </button>

          </form>

          <div className="test-account">
            <strong>
              Development account
            </strong>

            <p>
              Username: student2
            </p>

            <p>
              Password: Student@123
            </p>
          </div>

        </div>
      </div>
    );
  }

  /* DASHBOARD */

  return (
    <div className="dashboard">

      <header className="dashboard-header">

        <div>
          <h1>
            College Management System
          </h1>

          <p>
            Welcome back, {user.username}
          </p>
        </div>

        <button
          onClick={handleLogout}
          className="logout-button"
        >
          Logout
        </button>

      </header>

      <main className="dashboard-content">

        {/* USER DASHBOARD CARD */}

        <div className="welcome-card">

          <h2>
            Dashboard
          </h2>

          <p>
            You are successfully authenticated
            using Django JWT.
          </p>

          <div className="user-details">

            <div>
              <strong>
                Username
              </strong>

              <span>
                {user.username}
              </span>
            </div>

            <div>
              <strong>
                Email
              </strong>

              <span>
                {user.email}
              </span>
            </div>

            <div>
              <strong>
                Role
              </strong>

              <span>
                {user.role}
              </span>
            </div>

          </div>

        </div>

        {/* STUDENT INFORMATION */}

        {studentsLoading && (
          <div className="welcome-card">
            <h2>
              Loading Student Information...
            </h2>
          </div>
        )}

        {!studentsLoading &&
          students.length > 0 && (
            <div className="welcome-card">

              <h2>
                👨‍🎓 Student Information
              </h2>

              {students.map((student) => (
                <div
                  className="user-details"
                  key={student.id}
                >

                  <div>
                    <strong>
                      Student ID
                    </strong>

                    <span>
                      {student.student_id}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Name
                    </strong>

                    <span>
                      {student.username}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Email
                    </strong>

                    <span>
                      {student.email}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Department
                    </strong>

                    <span>
                      {student.department}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Course
                    </strong>

                    <span>
                      {student.course}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Semester
                    </strong>

                    <span>
                      {student.semester}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Gender
                    </strong>

                    <span>
                      {student.gender}
                    </span>
                  </div>

                  <div>
                    <strong>
                      Admission Date
                    </strong>

                    <span>
                      {student.admission_date}
                    </span>
                  </div>

                </div>
              ))}

            </div>
          )}

        {/* ATTENDANCE */}

        <div className="welcome-card">

          <h2>
            📋 Attendance
          </h2>

          {attendanceLoading && (
            <p>
              Loading attendance...
            </p>
          )}

          {attendanceError && (
            <div className="error-message">
              {attendanceError}
            </div>
          )}

          {!attendanceLoading &&
            !attendanceError &&
            attendance.length === 0 && (
              <p>
                No attendance records found.
              </p>
            )}

          {!attendanceLoading &&
            !attendanceError &&
            attendance.map((record) => (
              <div
                className="user-details"
                key={record.id}
              >

                <div>
                  <strong>
                    Subject
                  </strong>

                  <span>
                    {record.subject_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject Code
                  </strong>

                  <span>
                    {record.subject_code}
                  </span>
                </div>

                <div>
                  <strong>
                    Date
                  </strong>

                  <span>
                    {record.date}
                  </span>
                </div>

                <div>
                  <strong>
                    Status
                  </strong>

                  <span>
                    {record.status}
                  </span>
                </div>

                <div>
                  <strong>
                    Remarks
                  </strong>

                  <span>
                    {record.remarks}
                  </span>
                </div>

              </div>
            ))}

        </div>

        {/* FACULTY */}

        <div className="welcome-card">

          <h2>
            👨‍🏫 Faculty Information
          </h2>

          {facultyLoading && (
            <p>
              Loading faculty information...
            </p>
          )}

          {facultyError && (
            <div className="error-message">
              {facultyError}
            </div>
          )}

          {!facultyLoading &&
            !facultyError &&
            faculty.length === 0 && (
              <p>
                No faculty records found.
              </p>
            )}

          {!facultyLoading &&
            !facultyError &&
            faculty.map((member) => (
              <div
                className="user-details"
                key={member.id}
              >

                <div>
                  <strong>
                    Employee ID
                  </strong>

                  <span>
                    {member.employee_id}
                  </span>
                </div>

                <div>
                  <strong>
                    Name
                  </strong>

                  <span>
                    {member.username}
                  </span>
                </div>

                <div>
                  <strong>
                    Email
                  </strong>

                  <span>
                    {member.email}
                  </span>
                </div>

                <div>
                  <strong>
                    Department
                  </strong>

                  <span>
                    {member.department}
                  </span>
                </div>

                <div>
                  <strong>
                    Designation
                  </strong>

                  <span>
                    {member.designation}
                  </span>
                </div>

                <div>
                  <strong>
                    Qualification
                  </strong>

                  <span>
                    {member.qualification}
                  </span>
                </div>

                <div>
                  <strong>
                    Joining Date
                  </strong>

                  <span>
                    {member.joining_date}
                  </span>
                </div>

                <div>
                  <strong>
                    Experience
                  </strong>

                  <span>
                    {member.experience_years} years
                  </span>
                </div>

              </div>
            ))}

        </div>

        {/* TIMETABLE */}

        <div className="welcome-card">

          <h2>
            📅 Timetable
          </h2>

          {timetableLoading && (
            <p>
              Loading timetable...
            </p>
          )}

          {timetableError && (
            <div className="error-message">
              {timetableError}
            </div>
          )}

          {!timetableLoading &&
            !timetableError &&
            timetable.length === 0 && (
              <p>
                No timetable records found.
              </p>
            )}

          {!timetableLoading &&
            !timetableError &&
            timetable.map((item) => (
              <div
                className="user-details"
                key={item.id}
              >

                <div>
                  <strong>
                    Day
                  </strong>

                  <span>
                    {item.day}
                  </span>
                </div>

                <div>
                  <strong>
                    Time
                  </strong>

                  <span>
                    {item.start_time} - {item.end_time}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject
                  </strong>

                  <span>
                    {item.subject_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject Code
                  </strong>

                  <span>
                    {item.subject_code}
                  </span>
                </div>

                <div>
                  <strong>
                    Faculty
                  </strong>

                  <span>
                    {item.faculty_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Room
                  </strong>

                  <span>
                    {item.room}
                  </span>
                </div>

              </div>
            ))}

        </div>

        {/* EXAMINATIONS */}

        <div className="welcome-card">

          <h2>
            📝 Examinations
          </h2>

          {examinationsLoading && (
            <p>
              Loading examinations...
            </p>
          )}

          {examinationsError && (
            <div className="error-message">
              {examinationsError}
            </div>
          )}

          {!examinationsLoading &&
            !examinationsError &&
            examinations.length === 0 && (
              <p>
                No examinations found.
              </p>
            )}

          {!examinationsLoading &&
            !examinationsError &&
            examinations.map((exam) => (
              <div
                className="user-details"
                key={exam.id}
              >

                <div>
                  <strong>
                    Exam
                  </strong>

                  <span>
                    {exam.exam_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject
                  </strong>

                  <span>
                    {exam.subject_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject Code
                  </strong>

                  <span>
                    {exam.subject_code}
                  </span>
                </div>

                <div>
                  <strong>
                    Exam Type
                  </strong>

                  <span>
                    {exam.exam_type}
                  </span>
                </div>

                <div>
                  <strong>
                    Date
                  </strong>

                  <span>
                    {exam.exam_date}
                  </span>
                </div>

                <div>
                  <strong>
                    Time
                  </strong>

                  <span>
                    {exam.start_time} - {exam.end_time}
                  </span>
                </div>

                <div>
                  <strong>
                    Maximum Marks
                  </strong>

                  <span>
                    {exam.maximum_marks}
                  </span>
                </div>

                <div>
                  <strong>
                    Room
                  </strong>

                  <span>
                    {exam.room}
                  </span>
                </div>

              </div>
            ))}

        </div>

        {/* RESULTS */}

        <div className="welcome-card">

          <h2>
            🏆 Examination Results
          </h2>

          {resultsLoading && (
            <p>
              Loading results...
            </p>
          )}

          {resultsError && (
            <div className="error-message">
              {resultsError}
            </div>
          )}

          {!resultsLoading &&
            !resultsError &&
            results.length === 0 && (
              <p>
                No examination results found.
              </p>
            )}

          {!resultsLoading &&
            !resultsError &&
            results.map((result) => (
              <div
                className="user-details"
                key={result.id}
              >

                <div>
                  <strong>
                    Exam
                  </strong>

                  <span>
                    {result.exam_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Subject
                  </strong>

                  <span>
                    {result.subject_name}
                  </span>
                </div>

                <div>
                  <strong>
                    Maximum Marks
                  </strong>

                  <span>
                    {result.maximum_marks}
                  </span>
                </div>

                <div>
                  <strong>
                    Marks Obtained
                  </strong>

                  <span>
                    {result.marks_obtained}
                  </span>
                </div>

                <div>
                  <strong>
                    Grade
                  </strong>

                  <span>
                    {result.grade}
                  </span>
                </div>

                <div>
                  <strong>
                    Grade Point
                  </strong>

                  <span>
                    {result.grade_point}
                  </span>
                </div>

                <div>
                  <strong>
                    Result
                  </strong>

                  <span>
                    {result.result_status}
                  </span>
                </div>

                <div>
                  <strong>
                    Remarks
                  </strong>

                  <span>
                    {result.remarks}
                  </span>
                </div>

              </div>
            ))}

        </div>

        {/* MODULE CARDS */}

        <div className="module-grid">

          <div className="module-card">
            <span>👨‍🎓</span>
            <h3>
              Students
            </h3>
            <p>
              Manage student information
            </p>
          </div>

          <div className="module-card">
            <span>👨‍🏫</span>
            <h3>
              Faculty
            </h3>
            <p>
              Manage faculty information
            </p>
          </div>

          <div className="module-card">
            <span>📚</span>
            <h3>
              Academics
            </h3>
            <p>
              Courses and subjects
            </p>
          </div>

          <div className="module-card">
            <span>📅</span>
            <h3>
              Timetable
            </h3>
            <p>
              View class schedules
            </p>
          </div>

          <div className="module-card">
            <span>📝</span>
            <h3>
              Examinations
            </h3>
            <p>
              Manage examinations
            </p>
          </div>

          <div className="module-card">
            <span>🏆</span>
            <h3>
              Results
            </h3>
            <p>
              View examination results
            </p>
          </div>

        </div>

      </main>

    </div>
  );
}

export default App;