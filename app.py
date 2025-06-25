import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re

# Load the updated dataset
data = pd.read_csv('job_courses_updated.csv')
data.columns = data.columns.str.strip()

# Define skills for extraction
programming_languages = [
    "Python", "Java", "C++", "JavaScript", "C#", "Ruby", "PHP", "Swift",
    "Go", "Kotlin", "R", "TypeScript", "Scala", "Rust"
]
operating_systems = [
    "Windows", "Linux", "macOS", "Ubuntu", "Debian", "Fedora",
    "Red Hat", "CentOS", "Android", "iOS"
]

# Extract info from resume
def extract_information(resume_text):
    name_pattern = r'(?<=Name:)(.*?)(?=\n)'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    contact_pattern = r'\b\d{10}\b'

    name = re.search(name_pattern, resume_text)
    email = re.findall(email_pattern, resume_text)
    contact = re.findall(contact_pattern, resume_text)

    programming_skills_found = [skill for skill in programming_languages if re.search(r'\b' + re.escape(skill) + r'\b', resume_text, re.IGNORECASE)]
    operating_systems_found = [os for os in operating_systems if re.search(r'\b' + re.escape(os) + r'\b', resume_text, re.IGNORECASE)]

    return {
        'name': name.group(0).strip() if name else "Not found",
        'email': email[0] if email else "Not found",
        'contact': contact[0] if contact else "Not found",
        'programming_skills': ', '.join(programming_skills_found) if programming_skills_found else "Not found",
        'operating_systems': ', '.join(operating_systems_found) if operating_systems_found else "Not found"
    }

# Recommend jobs based on resume
def recommend_jobs_and_courses(resume_text):
    vectorizer = CountVectorizer()
    data['skills'] = data['skills'].apply(lambda x: x.replace(",", " "))
    skills_matrix = vectorizer.fit_transform(data['skills'].tolist() + [resume_text])
    cosine_sim = cosine_similarity(skills_matrix[-1], skills_matrix[:-1])
    recommended_indices = cosine_sim.argsort()[0][-3:][::-1]

    recommendations = []
    for idx in recommended_indices:
        courses_list = data.iloc[idx]['courses'].split(',')
        top_courses = ', '.join(courses_list[:3])  # Show top 3
        recommendations.append({
            'job_title': data.iloc[idx]['job_title'],
            'courses': top_courses,
            'youtube_link': data.iloc[idx]['youtube_link'],
            'free_course_link': data.iloc[idx]['free_course_link']
        })
    return recommendations

# Read resume file
def read_resume(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return ''.join([page.extract_text() for page in reader.pages])
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        st.error("Unsupported file type. Please upload a PDF or text file.")
        return None

# --- UI Styling ---
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(145deg, #8c8c8c, #525252);
        color: ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #1e1919;
        font-weight: 700;
        text-shadow: 0 1px 2px rgba(0,0,0,0.4);
    }

    .stButton > button {
        background-color: #5e60ce;
        color: white;
        border-radius: 10px;
        font-size: 15px;
        padding: 0.6em 1.4em;
        border: none;
        box-shadow: 0 0 10px rgba(94, 96, 206, 0.5);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #4a4ec4;
        transform: scale(1.05);
    }

    .info-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5em;
        margin: 1em 0;
        border-left: 4px solid #5e60ce;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    .info-box p {
        color: #000000;
        font-size: 15.5px;
        line-height: 1.7;
        margin: 0.5em 0;
    }

    a {
        color: #96f7d2;
        text-decoration: none;
        font-weight: 500;
    }

    a:hover {
        color: #b2ffe6;
        text-decoration: underline;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #5e60ce;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Streamlit Interface ---
st.title("💼 Resume Analyzer & Job Recommender")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    resume_text = read_resume(uploaded_file)
    if resume_text:
        extracted_info = extract_information(resume_text)

        st.markdown("### 🧠 Extracted Information")
        with st.container():
            st.markdown(f"""
            <div class="info-box">
                <p><strong>👤 Name:</strong> {extracted_info['name']}</p>
                <p><strong>📧 Email:</strong> {extracted_info['email']}</p>
                <p><strong>📱 Contact:</strong> {extracted_info['contact']}</p>
                <p><strong>💻 Programming Skills:</strong> {extracted_info['programming_skills']}</p>
                <p><strong>🖥️ Operating Systems:</strong> {extracted_info['operating_systems']}</p>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔍 Analyze"):
            recommendations = recommend_jobs_and_courses(resume_text)
            st.markdown("### 🎯 Top Job Recommendations")
            for rec in recommendations:
                st.markdown(f"""
                <div class="info-box">
                    <p><strong>🧑‍💼 Job Title:</strong> {rec['job_title']}</p>
                    <p><strong>📚 Top 3 Courses:</strong> {rec['courses']}</p>
                    <p>▶️ <a href="{rec['youtube_link']}" target="_blank">YouTube Channel</a></p>
                    <p>🎓 <a href="{rec['free_course_link']}" target="_blank">Course Website</a></p>
                </div>
                """, unsafe_allow_html=True)
