
import streamlit as st
import PyPDF2
import re
import os
from io import BytesIO
from dotenv import load_dotenv
from openai import OpenAI
from docx import Document
from docx.shared import Inches

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI OBE Intelligence Platform")

st.title("AI Powered OBE Course File Refinement System")

vision_file = st.file_uploader(
    "Upload Vision Mission PDF",
    type=["pdf"]
)

peo_file = st.file_uploader(
    "Upload PEO PO PSO PDF",
    type=["pdf"]
)

course_file = st.file_uploader(
    "Upload Course File PDF",
    type=["pdf"]
)

def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:

            extracted = extracted.replace("\n", " ")

            extracted = re.sub(r"\s+", " ", extracted)

            text += extracted + "\n\n"

    return text

def generate_refined_syllabus(
    vision_text,
    peo_text,
    course_text
):

    prompt = f"""
You are an NBA and OBE expert.

Analyze the uploaded documents and generate a FULLY REFINED COURSE FILE
in proper university syllabus format.

STRICT REQUIREMENTS:

1. Rewrite professionally:
- Prerequisite
- Course Objectives
- Course Outcomes

2. Generate:
- Updated CO-PO Mapping
- Updated CO-PO Justification
- Updated Pedagogy
- Student Centric TL methods
- ICT enabled tools topic wise
- Unit wise innovative assignments
- Mini projects
- Experiential learning activities
- Industry oriented activities
- SDG mapping

3. Ensure complete alignment with:
- Vision
- Mission
- PEO
- PO
- PSO

4. Ensure Bloom Taxonomy correctness.

5. Keep format suitable for NBA/NAAC documentation.

6. Generate polished academic content.

VISION & MISSION:
{vision_text}

PEO PO PSO:
{peo_text}

COURSE FILE:
{course_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert academic OBE consultant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

def create_docx(content):

    document = Document()

    document.add_heading(
        "AI Generated Refined OBE Course File",
        level=1
    )

    paragraphs = content.split("\n")

    for para in paragraphs:

        para = para.strip()

        if para:

            if para.isupper():

                document.add_heading(para, level=2)

            else:

                document.add_paragraph(para)

    buffer = BytesIO()

    document.save(buffer)

    buffer.seek(0)

    return buffer

if (
    vision_file is not None and
    peo_file is not None and
    course_file is not None
):

    try:

        with st.spinner("Reading PDFs..."):

            vision_text = extract_text_from_pdf(vision_file)

            peo_text = extract_text_from_pdf(peo_file)

            course_text = extract_text_from_pdf(course_file)

        with st.spinner("AI is generating refined syllabus..."):

            refined_output = generate_refined_syllabus(
                vision_text,
                peo_text,
                course_text
            )

        st.success("Refined syllabus generated successfully")

        st.markdown(refined_output)

        docx_file = create_docx(refined_output)

        st.download_button(
            label="Download Refined DOCX File",
            data=docx_file,
            file_name="Refined_OBE_Course_File.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:

        st.error(f"Error: {e}")
