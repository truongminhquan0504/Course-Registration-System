import bcrypt from "bcryptjs";

import { db } from "./store.js";

/**
 * Tạo lại toàn bộ dữ liệu mẫu. Chạy bằng `npm run seed`.
 * Mật khẩu demo cho MỌI tài khoản: 123456
 */

const DEMO_PASSWORD_HASH = bcrypt.hashSync("123456", 10);

const users = [
  {
    id: 1,
    name: "Quản trị hệ thống",
    email: "admin@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "ADMIN",
    student_code: null,
    created_at: new Date().toISOString(),
  },
  {
    id: 2,
    name: "GV. Nguyễn Văn An",
    email: "teacher1@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "TEACHER",
    student_code: null,
    created_at: new Date().toISOString(),
  },
  {
    id: 3,
    name: "GV. Trần Thị Bình",
    email: "teacher2@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "TEACHER",
    student_code: null,
    created_at: new Date().toISOString(),
  },
  {
    id: 4,
    name: "GV. Lê Văn Cường",
    email: "teacher3@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "TEACHER",
    student_code: null,
    created_at: new Date().toISOString(),
  },
  {
    id: 5,
    name: "Phạm Văn Đức",
    email: "sv1@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "STUDENT",
    student_code: "B21DCCN001",
    created_at: new Date().toISOString(),
  },
  {
    id: 6,
    name: "Hoàng Thị Em",
    email: "sv2@ptit.edu.vn",
    password: DEMO_PASSWORD_HASH,
    role: "STUDENT",
    student_code: "B21DCCN002",
    created_at: new Date().toISOString(),
  },
];

db.reset({ users, subjects: [], classes: [], registrations: [] });

console.log("Đã tạo dữ liệu mẫu thành công.");
console.log("Tài khoản demo (mật khẩu chung: 123456):");
console.log("  Admin    : admin@ptit.edu.vn");
console.log("  Giảng viên: teacher1@ptit.edu.vn / teacher2@ptit.edu.vn / teacher3@ptit.edu.vn");
console.log("  Sinh viên : sv1@ptit.edu.vn / sv2@ptit.edu.vn");
