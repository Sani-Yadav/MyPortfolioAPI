# MyPortfolioAPI

Personal portfolio API built with Django & Django REST Framework (DRF) to manage About, Resume, Skills, Projects, Education, Experience, and Contact data.

---

## 🚀 Features
- **About Section:** Manage your personal bio, profile image, and resume.
- **Skills:** Add, update, and list your technical skills.
- **Projects:** Showcase your projects with descriptions and GitHub links.
- **Education:** Track your academic background.
- **Experience:** List your professional experience.
- **Contact:** Receive messages from your portfolio site.
- **Token Authentication:** Secure API endpoints with DRF's token auth.
- **Admin Panel:** Manage all data via Django admin.

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be changed)
- **Authentication:** Token-based (DRF)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sani-Yadav/MyPortfolioAPI.git
   cd MyPortfolioAPI
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## 🔑 API Authentication
- Obtain a token via `/api/login/` endpoint (POST username & password).
- Use the token in the `Authorization` header for protected endpoints:
  ```
  Authorization: Token your_token_here
  ```
http://127.0.0.1:8000/api/skills/
---

## 📚 API Endpoints
| Endpoint                | Methods        | Description                  |
|------------------------ |---------------|------------------------------|
| `/api/about/`           | GET, POST, PUT, PATCH | About info CRUD         |
| `/api/skills/`          | GET, POST     | List/Create skills           |
| `/api/skills/<id>/`     | GET, PUT, PATCH, DELETE | Skill detail/update/delete |
| `/api/projects/`        | GET, POST     | List/Create projects         |
| `/api/projects/<id>/`   | GET, PUT, PATCH, DELETE | Project detail/update/delete |
| `/api/education/`       | GET, POST     | List/Create education        |
| `/api/education/<id>/`  | GET, PUT, PATCH, DELETE | Education detail/update/delete |
| `/api/experience/`      | GET, POST     | List/Create experience       |
| `/api/experience/<id>/` | GET, PUT, PATCH, DELETE | Experience detail/update/delete |
| `/api/contact/`         | POST          | Send a contact message       |
| `/api/login/`           | POST          | Obtain auth token            |

---

## 🖥️ Admin Panel
- Access at `/admin/` with your superuser credentials.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙋‍♂️ Author
**Sani Yadav**  
[GitHub](https://github.com/Sani-Yadav) 
