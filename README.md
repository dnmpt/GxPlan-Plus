# 🚀 GxPlan+
### *Planning a Collaborative Compliance.*

**GxPlan+** is a web-based project and task management system designed for regulated industries that demand both **team collaboration** and **compliance traceability**.  
Built with **Python (Django framework)** and a modern **Bootstrap interface**, GxPlan+ extends the original *GxPlan* philosophy — *Plan in Compliance* — into the collaborative domain, enabling multiple users to plan, track, and document their work together while maintaining full auditability and data integrity.

---

## 🌐 Key Features

- **Collaborative Project and Task Management**  
  Manage multiple projects with shared access among authenticated users.  
  Each task includes start and end dates, responsible user(s), and weighted priority based on *urgency*, *compliance*, and *effort*.

- **Dynamic Prioritization Engine**  
  Integrated priority algorithm combining compliance criticality, time constraints, and workload for adaptive project management.

- **Progression Tracker**  
  Real-time progress monitoring for tasks and projects, including visual dashboards and percentage-based completion tracking.

- **Audit Trail & Traceable Notes**  
  Each note added to a task or project is automatically timestamped and attributed to its author, ensuring traceability and accountability.

- **User Authentication & Role Management**  
  Built-in Django authentication with role-based access control (RBAC) for hierarchical and secure collaboration:
  - *Administrators* – full access to configuration, users, and all projects  
  - *Project Managers* – can create and assign tasks, manage timelines  
  - *Contributors* – can update progress and add compliant notes  
  - *Viewers* – read-only access for oversight and audits

- **Modern Web Interface (Bootstrap)**  
  Responsive, clean, and intuitive design powered by Bootstrap 5.  
  Includes dashboards with color-coded indicators, icons, and images for quick project and task identification.


---

## ⚙️ Technical Overview

| Component | Description |
|------------|--------------|
| **Python 3.x** | Core programming language |
| **Django Framework** | Web backend (MVC/MVT architecture) |
| **SQLite / MariaDB** | Database options (default: SQLite for testing) |
| **Bootstrap 5** | Frontend styling and responsive dashboards |
| **Django ORM** | Object-relational mapping for models |
| **Django Auth** | Built-in user authentication and session management |

---

## 🧩 System Modules

```
/gxplan_plus/             → Main Django project configuration
/apps/
    ├── projects/         → Project and task management
    ├── notes/            → Traceable notes and audit trail
    ├── users/            → Authentication, roles, and permissions
    ├── dashboard/        → Bootstrap-powered dashboards
/templates/               → HTML templates (Bootstrap 5)
/static/                  → CSS, JS, and media files
/db.sqlite3               → Default development database
/manage.py                → Django management script
/LICENSE.md               → MIT License
```

---

## ⚡ Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/GxPlan-Plus.git
   cd GxPlan-Plus
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv env
   . env/bin/activate   # Linux / macOS
   env\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r src/site1-main/requirements/dev.txt
   or simpler (Linux):
   cd commands
   ./packages_dev.sh
   ```

4. **Run database migrations**
   ```bash
   cd ..
   cd src/site1-main
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)


8. **Enter data**
   Access Administration of Django : [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   with 'admin' user and create other users or enter categories

   **NOTE:**
   This application is in development and 'category' management is not yet implemented.
   So, the high level object ('category') must be entered and associated to an user using this option.
---

## 🧠 Philosophy — “Planning a Collaborative Compliance”

**GxPlan+** brings together two essential forces in modern industry:
- the **discipline** of *compliance planning*, and  
- the **efficiency** of *collaborative teamwork*.  

Its motto — *Planning a Collaborative Compliance* — reflects the belief that compliance is not an individual effort but a **collective responsibility**, supported by tools that ensure transparency, structure, and shared ownership.

---

## 🧑‍💻 Author

**Duarte Mendes**  
© 2023-2025 Duarte Mendes — [https://github.com/dnmpt]

---

## 📜 License

This project is distributed under the terms of the **MIT License** — see [LICENSE.md](LICENSE.md) for details.  
> The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.

---

## 🧭 From GxPlan to GxPlan+

| Version | Platform | Focus | Users | Data Model |
|----------|-----------|--------|--------|-------------|
| **GxPlan** | Desktop (PureBasic) | Individual planning and prioritization | Single-user | Local SQLite |
| **GxPlan+** | Web (Django/Python) | Collaborative and compliant planning | Multi-user | Server-hosted DB |

---

## 🪶 Slogan

> **“Planning a Collaborative Compliance — because compliance works better together.”**
