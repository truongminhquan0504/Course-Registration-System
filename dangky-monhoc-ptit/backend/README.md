# Backend — Tài khoản và đăng nhập

Node.js + Express. Dữ liệu lưu tại `src/data/db.json` (tự tạo khi seed/chạy
lần đầu).

## Cài đặt

```bash
npm install
cp .env.example .env
npm run seed     # tạo dữ liệu mẫu
npm run dev       # chạy với --watch, tự restart khi sửa code
# hoặc: npm start
```

Mặc định chạy tại `http://localhost:5000`, tất cả API nằm dưới `/api`.

## API

- `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/auth/me`
- `GET /api/users`, `PUT /api/users/:id/role` (Admin)

## Ghi chú thiết kế

- Mật khẩu băm bằng `bcryptjs` (thuần JS, không cần biên dịch native — chạy
  ổn định trên mọi môi trường).
- Muốn xóa toàn bộ dữ liệu và làm lại từ đầu: chạy lại `npm run seed`.
