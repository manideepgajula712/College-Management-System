import { useState } from "react";
import { login, logout } from "./services/api";
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

      localStorage.setItem("user", JSON.stringify(loggedInUser));

      setUser(loggedInUser);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    logout();

    localStorage.removeItem("user");

    setUser(null);
    setUsername("");
    setPassword("");
  };

  if (!user) {
    return (
      <div className="login-page">
        <div className="login-card">

          <div className="login-header">
            <div className="logo">🎓</div>

            <h1>College Management System</h1>

            <p>Sign in to continue</p>
          </div>

          <form onSubmit={handleLogin}>

            <div className="form-group">
              <label>Username</label>

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
              <label>Password</label>

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
              {loading ? "Signing in..." : "Sign In"}
            </button>

          </form>

          <div className="test-account">
            <strong>Development account</strong>

            <p>Username: student2</p>
            <p>Password: Student@123</p>
          </div>

        </div>
      </div>
    );
  }

  return (
    <div className="dashboard">

      <header className="dashboard-header">

        <div>
          <h1>College Management System</h1>

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

        <div className="welcome-card">

          <h2>Dashboard</h2>

          <p>
            You are successfully authenticated
            using Django JWT.
          </p>

          <div className="user-details">

            <div>
              <strong>Username</strong>
              <span>{user.username}</span>
            </div>

            <div>
              <strong>Email</strong>
              <span>{user.email}</span>
            </div>

            <div>
              <strong>Role</strong>
              <span>{user.role}</span>
            </div>

          </div>

        </div>

        <div className="module-grid">

          <div className="module-card">
            <span>👨‍🎓</span>
            <h3>Students</h3>
            <p>Manage student information</p>
          </div>

          <div className="module-card">
            <span>👨‍🏫</span>
            <h3>Faculty</h3>
            <p>Manage faculty information</p>
          </div>

          <div className="module-card">
            <span>📚</span>
            <h3>Academics</h3>
            <p>Courses and subjects</p>
          </div>

          <div className="module-card">
            <span>📅</span>
            <h3>Timetable</h3>
            <p>View class schedules</p>
          </div>

          <div className="module-card">
            <span>📝</span>
            <h3>Examinations</h3>
            <p>Manage examinations</p>
          </div>

          <div className="module-card">
            <span>🏆</span>
            <h3>Results</h3>
            <p>View examination results</p>
          </div>

        </div>

      </main>

    </div>
  );
}

export default App;