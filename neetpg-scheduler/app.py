import streamlit as st
import pandas as pd

st.set_page_config(page_title="NEET PG AI Planner", layout="wide")
st.title("📊 AI-Powered NEET PG Study Planner")

st.sidebar.header("🧠 Your Profile")
target_exam = st.sidebar.text_input("Target Exam", "NEET PG 2025")
study_hours = st.sidebar.slider("Daily Study Hours", 1, 12, 6)
rank_goal = st.sidebar.selectbox("Rank Goal", ["Top 100", "Top 1000", "Qualify"])

subjects = ['Pharmacology', 'Pathology', 'PSM', 'Anatomy', 'Medicine']
progress = []

for subj in subjects:
    st.subheader(subj)
    complete = st.slider(f"Completion % - {subj}", 0, 100, 50, key=f"{subj}_c")
    score = st.slider(f"Mock Score % - {subj}", 0, 100, 50, key=f"{subj}_s")
    mode = st.selectbox(f"Preferred Mode - {subj}", ['Video', 'MCQ', 'PDF', 'Live Class'], key=f"{subj}_m")
    progress.append([subj, complete, score, mode])

df = pd.DataFrame(progress, columns=['Subject', 'Completion (%)', 'Mock Score (%)', 'Preferred Mode'])

# 🔁 AI Logic
def suggest(row):
    if row['Mock Score (%)'] < 50:
        return f"🔁 Revise {row['Subject']} using {row['Preferred Mode']}"
    elif row['Completion (%)'] < 50:
        return f"📚 Complete content of {row['Subject']}"
    else:
        return f"✅ {row['Subject']} – Weekly Review"

df['AI Suggestion'] = df.apply(suggest, axis=1)
st.write("### 💡 AI Suggestions")
st.dataframe(df)
