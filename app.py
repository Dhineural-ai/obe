import streamlit as st
import PyPDF2
import re
import os

from io import BytesIO

from dotenv import load_dotenv

from openai import OpenAI

from docx import Document

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.set_page_config(
    page_title="AI Curriculum Intelligence Platform",
    layout="wide"
)

st.title("AI Powered Curriculum Intelligence Platform")

st.markdown("""
This AI system performs:

- OBE curriculum evaluation
- syllabus redesign
- Bloom taxonomy validation
- CO-PO intelligence mapping
- pedagogy recommendation
- assessment strategy generation
- academic modernization
""")

vision_file = st.file_uploader(
    "Upload Vision & Mission PDF",
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


def generate_curriculum_intelligence_report(
    vision_text,
    peo_text,
    course_text
):

    prompt = f"""

You are a globally experienced:

- NBA expert
- NAAC expert
- Outcome Based Education consultant
- Bloom taxonomy specialist
- curriculum architect
- industry-aligned syllabus designer
- academic governance advisor

IMPORTANT:

DO NOT paraphrase the uploaded syllabus.

DO NOT simply rewrite uploaded content.

Instead:

CRITICALLY EVALUATE the uploaded syllabus.

Then redesign the course intelligently according to:

- global academic standards
- Bloom taxonomy
- Outcome Based Education
- industry expectations
- graduate competency expectations
- experiential learning
- student-centric learning
- PO/PSO attainment
- mission alignment
- employability
- innovation
- real-world application

STRICTLY FOLLOW THIS PROCESS:

STEP 1:
Analyze weaknesses in uploaded syllabus.

Detect:
- weak COs
- non measurable verbs
- Bloom taxonomy mismatch
- weak pedagogy
- unrealistic mapping
- lack of industry relevance
- lack of experiential learning
- poor curriculum alignment

STEP 2:
Determine what students SHOULD ACTUALLY learn in this course
at this semester level.

STEP 3:
Generate IDEAL version of:

- prerequisite
- course objectives
- course outcomes

Ensure:
- measurable COs
- proper Bloom distribution
- practical competency development
- analytical skills
- problem solving
- real-world application

STEP 4:
Generate:

- Correct CO-PO mapping matrix
- Correct CO-PSO mapping matrix
- Realistic mapping strengths
- Proper mapping justifications

IMPORTANT:
Mappings must NOT be random.
Mappings must be based on actual competency contribution.

STEP 5:
Generate UNIT-WISE:

- student-centric TL pedagogy
- active learning strategy
- experiential learning activity
- inquiry-based learning
- collaborative learning
- industry-oriented activity
- problem-solving strategy
- peer teaching activity
- ICT enabled tools

STEP 6:
Generate 3 HIGH-VALUE TERM WORKS.

Each term work must:
- support CO attainment
- support PO/PSO attainment
- improve employability
- improve analytical ability
- improve practical competency
- improve innovation

STEP 7:
Generate:

- mini projects
- real-world applications
- interdisciplinary activities
- SDG mapping
- assessment strategy
- rubrics suggestion

STEP 8:
Generate FINAL REFINED COURSE FILE.

IMPORTANT:
The output should look like a REAL modern university syllabus.

The output should be:
- professional
- structured
- accreditation ready
- globally aligned
- academically meaningful

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
                "content": "You are a senior global curriculum intelligence expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


def create_docx(content):

    document = Document()

    document.add_heading(
        "AI Generated Curriculum Intelligence Report",
        level=1
    )

    paragraphs = content.split("\n")

    for para in paragraphs:

        para = para.strip()

        if para:

            if len(para) < 100 and (
                para.isupper() or
                para.endswith(":")
            ):

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

        with st.spinner("Reading uploaded documents..."):

            vision_text = extract_text_from_pdf(vision_file)

            peo_text = extract_text_from_pdf(peo_file)

            course_text = extract_text_from_pdf(course_file)

        with st.spinner("AI is redesigning curriculum intelligently..."):

            refined_output = generate_curriculum_intelligence_report(
                vision_text,
                peo_text,
                course_text
            )

        st.success(
            "AI Curriculum Intelligence Report Generated Successfully"
        )

        st.markdown(refined_output)

        docx_file = create_docx(refined_output)

        st.download_button(
            label="Download Editable DOCX Report",
            data=docx_file,
            file_name="AI_Curriculum_Intelligence_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:

        st.error(f"Error: {e}")
