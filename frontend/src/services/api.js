const API_BASE_URL = "http://127.0.0.1:8000/api";

export async function login(username, password) {
  const response = await fetch(`${API_BASE_URL}/auth/login/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      password,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Invalid username or password"
    );
  }

  localStorage.setItem("access_token", data.access);
  localStorage.setItem("refresh_token", data.refresh);

  return data;
}

export async function getProfile() {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/auth/profile/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error("Unable to load profile");
  }

  return response.json();
}

export async function apiFetch(endpoint, options = {}) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...(options.headers || {}),
    },
  });

  if (!response.ok) {
    const data = await response.json().catch(() => ({}));

    throw new Error(
      data.detail || `API request failed: ${response.status}`
    );
  }

  return response.json();
}

export function logout() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("user");
}