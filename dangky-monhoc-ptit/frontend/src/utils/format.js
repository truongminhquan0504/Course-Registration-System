export function formatDate(isoString) {
  if (!isoString) return "";
  return new Date(isoString).toLocaleDateString("vi-VN", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });
}

export const ROLE_LABELS = {
  STUDENT: "Sinh viên",
  TEACHER: "Giảng viên",
  ADMIN: "Quản trị viên",
};
