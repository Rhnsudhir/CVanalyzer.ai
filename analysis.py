import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

from pdf import extractpdf  # Refer pdf.py file 

# Configure the api key
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

# Call the model

model = genai.GenerativeModel('gemini-1.5-flash')

# Create a def function to analyze the PDF and JD

def analyze_resume(pdf_doc, job_des):
    
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)
        st.write('Extracted Successfully✅')
        
    else:
        st.warning('Drop file in PDF format')
        
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_des} and get ATS score inn scale of 0 to 100. 
                                       Generate results in bullet points''')
    good_fit = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_des} and say if I am a good fit for the job or not.
                                       Generate results in bullet points''')
    swot_analysis = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_des} and provide SWOT analysis. 
                                       Generate results in bullet points''')
    prob = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_des} and give the probability (in percent) 
                                       of getting hired. Generate results in bullet points''')

    return {st.write(ats_score.text),
           st.write(good_fit.text),
           st.write(swot_analysis.text),
           st.write(prob.text)}
           
