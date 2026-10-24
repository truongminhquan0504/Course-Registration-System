import { useEffect } from "react";
import { Navigate, Route, Routes, useLocation } from "react-router-dom";

import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";
import { useAuth } from "./context/AuthContext";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ManageUsers from "./pages/admin/ManageUsers";
import { ROLE_LABELS } from "./utils/format";

/** Đổi trang thì luôn cuộn lên đầu. */
function ScrollHandler() {
  const location = useLocation();

  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [location.pathname]);

  return null;
}

function AccountHome() {
  const { user } = useAuth();

  return (
    <section className="page">
      <div className="container">
        <div className="page__header">
          <div>
            <h1 className="page__title">Thông tin tài khoản</h1>
            <p className="page__subtitle">Xin chào, {user.name}.</p>
          </div>
        </div>
        <div className="card">
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>Vai trò:</strong> {ROLE_LABELS[user.role]}</p>
          {user.student_code && <p><strong>Mã sinh viên:</strong> {user.student_code}</p>}
        </div>
      </div>
    </section>
  );
}

export default function App() {
  return (
    <>
      <ScrollHandler />
      <Navbar />
      <main>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <AccountHome />
              </ProtectedRoute>
            }
          />
          <Route
            path="/quan-tri/tai-khoan"
            element={
              <ProtectedRoute roles={["ADMIN"]}>
                <ManageUsers />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </>
  );
}
