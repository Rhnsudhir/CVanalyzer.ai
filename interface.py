import streamlit as st
from analysis import analyze_resume  

st.title('CV Analyzer🎯')

st.header('This page helps you to compare your resume with the given Job Description')

st.sidebar.subheader('Drop your resume here 📑')

pdf_doc = st.sidebar.file_uploader('Click here to browse', type=['pdf'])

st.sidebar.markdown('Designed by Rohan Sudhir')
st.sidebar.markdown("LinkedIn : 'www.linkedin.com/in/rohan-sudhir-5b818134b'")

job_des = st.text_area('Copy and Paste the Job Description here', max_chars=10000)

submit = st.button('Generate ATS Score')

if submit:
    with st.spinner('Getting Results...'):
       analyze_resume(pdf_doc, job_des)
    