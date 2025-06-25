# 📊 KSA Data Visualisation Dashboard

A modern, responsive, and interactive data analytics dashboard built using **React**, **Tailwind CSS**, **Plotly**, and **Supabase**. Inspired by Vuexy admin UI, this dashboard visualizes key variables like **intensity**, **likelihood**, and **relevance** from a JSON dataset using dynamic filters, KPIs, and charts.

---

## 🚀 Features

- ✅ **Login Interface** with fake auth
- 🌙 **Dark/Light Mode** toggle
- 🎯 **KPI Summary Cards**: Total Entries, Avg Intensity, Avg Relevance
- 📊 **Interactive Charts** with Plotly.js
- 🔍 **Dynamic Filtering** by topic, region, country, sector, city, etc.
- 📂 **Supabase JSON Upload** script included
- 🎨 **Clean UI** with animated cards, sidebar, and hover effects

---

## 🖼️ Screenshots

### 🔐 Login Page
![Login Page](./frontend/LoginPage_ScreenShot.png)

### 📊 Dashboard Overview
![Dashboard](./frontend/Dashboard_ScreenShot.png)

### 🧾 Supabase Database Structure
![Database](./frontend/Database_ScreenShot.png)

---

## 🧰 Tech Stack

- **Frontend:** React.js + Tailwind CSS
- **Charts:** Plotly.js
- **State Management:** React Hooks
- **Backend API:** Supabase + FastAPI
- **Auth:** Dummy logic for now
- **Deployment:** Vercel / GitHub Pages-ready

---

## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/data_visualisation_dashboard.git
cd data_visualisation_dashboard/frontend

# 2. Install frontend dependencies
npm install

# 3. Run the frontend
npm run dev
To upload data to Supabase (optional):
cd ../backend
pip install -r requirements.txt
python upload_to_supabase.py

---
📧 Contact
Made with ❤️ by ![github.com/nigam1010]

### ✅ To Use:

1. Replace `YOUR_USERNAME` with your GitHub username.
2. Place the `README.md` at the root of your repo (`data_visualisation_dashboard/README.md`).
3. Commit and push:

```bash
git add README.md
git commit -m "Add complete README with screenshots and features"
git push
