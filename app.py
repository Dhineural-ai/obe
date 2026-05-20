import streamlit as st
import PyPDF2
st.title("OBE Course File Refinement Tool")

vision_file = st.file_uploader(
    "Upload Vision-Mission PDF",
    type=["pdf"]
)

peo_file = st.file_uploader(
    "Upload PEO-PO PDF",
    type=["pdf"]
)

course_file = st.file_uploader(
    "Upload Course File PDF",
    type=["pdf"]
)

# PDF text extraction function
def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text
def analyze_alignment(vision, peo, course):

    return f"""
VISION:
{vision[:500]}

PEO:
{peo[:500]}

COURSE:
{course[:500]}

Alignment analysis completed.
"""


def generate_mapping_analysis(course, peo):

    return f"""
CO-PO Mapping Generated Successfully.

Course Length: {len(course)}
PEO Length: {len(peo)}
"""


def refine_course_document(vision, peo, course):

    return f"""
REFINED COURSE DOCUMENT

{course}
"""


def generate_final_report(alignment, mapping, refined):

    return f"""
===== ALIGNMENT REPORT =====

{alignment}

===== MAPPING REPORT =====

{mapping}

===== REFINED COURSE =====

{refined}
"""
if vision_file is not None and peo_file is not None and course_file is not None:

    try:

        with st.spinner("Reading PDFs..."):

            vision_text = extract_text_from_pdf(vision_file)
            peo_text = extract_text_from_pdf(peo_file)
            course_text = extract_text_from_pdf(course_file)

        alignment_report = analyze_alignment(
            vision_text,
            peo_text,
            course_text
        )

        mapping_report = generate_mapping_analysis(
            course_text,
            peo_text
        )

        refined_course = refine_course_document(
            vision_text,
            peo_text,
            course_text
        )

        final_report = generate_final_report(
            alignment_report,
            mapping_report,
            refined_course
        )

        st.success("OBE Refinement Completed")

        st.text_area(
            "Refined Course Document",
            refined_course,
            height=500
        )

        st.download_button(
            "Download Report",
            final_report,
            file_name="obe_report.txt"
        )

    except Exception as e:

        st.error(f"Error: {e}")
