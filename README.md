# Course Registration System

Ứng dụng đăng ký học phần viết bằng Django.

## Chạy dự án

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver
```

Mở `http://127.0.0.1:8000/registrations/courses/`.

Tạo tài khoản quản trị bằng `python manage.py createsuperuser` nếu cần.
