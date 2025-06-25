
# 💼 Resume Analyzer & Job Recommender

An intelligent Streamlit app that analyzes resumes, extracts key information, and recommends the top 3 relevant jobs with high-quality, **free** online learning resources.

![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python)

---

## 🚀 Features

- 📄 Resume parsing (PDF or TXT)
- 🧠 Skill extraction (Programming + OS)
- 🎯 Job + Course matching based on cosine similarity
- 📚 Shows top 3 courses + free resources (YouTube, Web)
- 💻 Sleek UI with styled layout

---

## 📷 Screenshots

### 🔼 Resume Upload + Extracted Info
![Resume Upload](oo=1.png)

### 🎯 Top Job Recommendations
![Recommendations](00=2.png)

---

## 📁 Project Structure

```
├── app.py                   # Streamlit app file
├── job_courses_updated.csv # Job-skill-course dataset
├── README.md                # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install the dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, use:
```bash
pip install streamlit pandas scikit-learn PyPDF2
```

### 3. Launch the app
```bash
streamlit run app.py
```

---

## 📊 About the Dataset

The `job_courses_updated.csv` file includes:
- ✅ `job_title`
- 🧠 `skills`
- 🎓 `courses`
- ▶️ `youtube_link`
- 🌐 `free_course_link`

---

## 🧪 Built With

- Python 🐍
- Streamlit 🌐
- scikit-learn 🤖
- pandas 🧾
- PyPDF2 📄

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Course and job data sourced from open platforms such as [freeCodeCamp](https://www.freecodecamp.org), [YouTube](https://youtube.com), and [Coursera](https://coursera.org).

