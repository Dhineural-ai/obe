import streamlit as st

from utils.pdf_reader import extract_text_from_pdf

from agents.bloom_agent import evaluate_bloom_levels
from agents.pedagogy_agent import suggest_pedagogy
from agents.ict_agent import suggest_ict_tools
from agents.assignment_agent import generate_assignments
from agents.report_agent import generate_report

st.set_page_config(page_title="OBE Intelligence Platform")

st.title("AI-Powered OBE Intelligence Platform")

st.subheader("Institutional Inputs")

vision_file = st.file_uploader("Upload Vision & Mission PDF")
peo_file = st.file_uploader("Upload PEO/PO/PSO PDF")

university_website = st.text_input("University Website")

st.subheader("Course File Upload")

course_file = st.file_uploader("Upload Course PDF")

if course_file:

    st.success("Course Uploaded Successfully")

    try:
        course_text = extract_text_from_pdf(course_file)

        st.subheader("AI Evaluation Running...")

        bloom_results = evaluate_bloom_levels(course_text)

        pedagogy_results = suggest_pedagogy(bloom_results)

        ict_results = suggest_ict_tools(course_text)

        assignments = generate_assignments(course_text)

        final_report = generate_report(
            bloom_results,
            pedagogy_results,
            ict_results,
            assignments
        )

        st.subheader("AI Evaluation Report")

        st.text_area(
            "Generated Report",
            final_report,
            height=700
        )

    except Exception as e:
        st.error(f"Error: {e}")
