# Tài khoản và đăng nhập — PTIT

Dự án gồm API Node.js/Express và giao diện React/Vite, tập trung vào đăng ký,
đăng nhập, xác thực JWT và quản lý tài khoản theo vai trò.

## Chạy dự án

Backend:

```bash
cd backend
npm install
cp .env.example .env
npm run seed
npm run dev
```

Frontend (mở terminal khác):

```bash
cd frontend
npm install
npm run dev
```

API mặc định chạy tại `http://localhost:5000/api`; giao diện tại
`http://localhost:5173`. Có thể cấu hình `JWT_SECRET` trong `backend/.env` và
`VITE_API_URL` trong `frontend/.env`.

## Chức năng

- Đăng ký tài khoản sinh viên, đăng nhập và xem thông tin tài khoản.
- Xác thực phiên đăng nhập bằng JWT.
- Quản trị viên có thể xem tài khoản và cập nhật vai trò.

Tài khoản mẫu (mật khẩu chung `123456`): `admin@ptit.edu.vn`,
`teacher1@ptit.edu.vn`, `teacher2@ptit.edu.vn`, `teacher3@ptit.edu.vn`,
`sv1@ptit.edu.vn`, `sv2@ptit.edu.vn`.
