# 🚀 Render.com Deployment Checklist

## Ishni Boshlash Uchun:

### 1️⃣ **Terminal/PowerShell-da:**
```bash
# Git repository yaratish
git init
git add .
git commit -m "Django app ready for deployment"
```

### 2️⃣ **GitHub/GitLab-da:**
- Yangi repository yarating
- Bu repository-ga push qiling:
```bash
git remote add origin https://github.com/YOUR_USERNAME/test-app.git
git push -u origin main
```

### 3️⃣ **Render.com-da:**
- ✅ Akkaunt yarating (render.com)
- ✅ GitHub/GitLab-ni ulang
- ✅ **New Web Service** bosing
- ✅ Repositoriyasini tanlang
- ✅ Settings qo'shing:

```
Name: test-app
Environment: Python 3
Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start Command: gunicorn config.wsgi:application
```

### 4️⃣ **Environment Variables qo'shing:**
```
DEBUG=False
SECRET_KEY=django-insecure-YANGI-KALIT-IXTIYORIY
ALLOWED_HOSTS=*.onrender.com
```

### 5️⃣ **PostgreSQL Database:**
- Render-da yangi PostgreSQL yarating
- `DATABASE_URL` avtomatik qo'shiladi

### ✅ **Tayyor!**
Deploy bosilsa, saytingiz 5-10 minutda live bo'ladi!

---

## 📁 Yaratilgan Fayllar:

| Fayl | Maqsadi |
|------|--------|
| `requirements.txt` | Python paketlari |
| `render.yaml` | Render sozlamalari |
| `Procfile` | Jarayon turi |
| `build.sh` | Build skripti |
| `.env.example` | Environment o'zgaruvchilar namunasi |
| `.gitignore` | Git istisno fayllar |
| `config/settings.py` | Yangilangan Django sozlamalari |
| `DEPLOYMENT.md` | To'liq qo'llanma |

---

**Savollar bo'lsa, `DEPLOYMENT.md` faylini o'qing!** 📖