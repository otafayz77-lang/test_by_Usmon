# Django Test Application - Render.com Deployment Guide

## 📋 Loyihani Render.com-ga Joyish Uchun Qadamlar

### **Step 1: Git Repository Yaratish**

Terminal/PowerShellda quyidagi buyruqlarni ishga tushiring:

```bash
git init
git add .
git commit -m "Initial commit - Django test app ready for deployment"
git branch -M main
```

Keyin GitHub, GitLab, yoki Gitea-da repository yarating va push qiling:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### **Step 2: Render.com-da Deploy Qilish**

1. [render.com](https://render.com) da akkaunt yarating yoki login qiling
2. Dashboard-da **"New"** tugmasini bosing
3. **"Web Service"** tanlang
4. GitHub/GitLab repositoriyasini ulang
5. Quyidagi sozlamalarni qilishni ta'minlang:

   - **Name:** test-app (yoki boshqa nom)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `gunicorn config.wsgi:application`

6. **Environment Variables** (Settings > Environment) qo'shing:

```
DEBUG=False
SECRET_KEY=<keyni-ixtiyoriy-rang-qilgan-string-yozing>
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=<Render PostgreSQL dan oladi>
```

### **Step 3: Database Yaratish**

1. Render Dashboard-da **"New"** > **"PostgreSQL"** bosing
2. Database yarating (free plan tanlang)
3. Connection string Render tarafidan beriladi - uni `DATABASE_URL` ga qo'shing

### **Step 4: Admin Panel Yaratish (Ixtiyoriy)**

Render shell-da:

```bash
python manage.py createsuperuser
```

Keyin `/admin/` saytiga kiring

### **🔧 Mahalliy Ishlab Chiqishda (Development)**

```bash
python manage.py runserver
```

### **📦 Qanday Fayllar Yaratildi:**

- `requirements.txt` - Barcha kerakli paketlar
- `render.yaml` - Render deployment konfiguratsiyasi
- `.gitignore` - Git-dan istisno qilinadi fayllar
- `.env.example` - Environment o'zgaruvchilari namunasi
- `build.sh` - Build script
- `config/settings.py` - Yangilangan Django sozlamalari

### **⚠️ Muhim Eslatmalar:**

1. **SECRET_KEY o'zgartiring!** Yangi, xavfsiz kalit yarating
2. **DEBUG=False** production-da
3. **ALLOWED_HOSTS** ni to'g'ri sozlang
4. Database migrations avtomatik ishga tushadi

### **🔗 Foydalanish Uchun Link:**

Deployment tamamlanganidan so'ng, Render sizga URL beradi:
`https://your-app.onrender.com`

Hamma tayyor! 🚀