# Resume Analyzer & Job Recommender

A streamlined Streamlit application that analyzes resumes, extracts relevant skills, and recommends the top three job roles along with curated, **free** online learning resources to help users bridge skill gaps and upskill effectively.

---

## Features

- Parses resumes in PDF or TXT format  
- Extracts key skills including programming languages and operating systems  
- Matches profiles to job roles using cosine similarity  
- Recommends top 3 relevant courses with free online resources  
- Clean and user-friendly interface built with Streamlit  

---

## Project Structure

```
├── app.py                   # Main application script
├── job_courses_updated.csv # Dataset containing job roles, skills, and course links
├── README.md                # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install Dependencies
If a `requirements.txt` file is available:
```bash
pip install -r requirements.txt
```

Otherwise, install manually:
```bash
pip install streamlit pandas scikit-learn PyPDF2
```

### 3. Launch the Application
```bash
streamlit run app.py
```

---

## Dataset Overview

The `job_courses_updated.csv` file includes the following fields:
- `job_title`: Suggested job roles  
- `skills`: Required skills for each role  
- `courses`: Recommended learning resources  
- `youtube_link`: Tutorial links  
- `free_course_link`: Additional free online courses  

---

## Technologies Used

- Python  
- Streamlit  
- scikit-learn  
- pandas  
- PyPDF2  

---

## Acknowledgements

The application uses openly available job and course data compiled from platforms such as:
- [freeCodeCamp](https://www.freecodecamp.org)  
- [YouTube](https://youtube.com)  
- [Coursera](https://coursera.org)
