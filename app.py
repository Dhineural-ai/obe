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
This platform performs:
- Curriculum Intelligence Audit
- OBE Redesign
- CO Redesign
- Intelligent CO-PO Mapping
- Pedagogy Intelligence
- Assignment Intelligence
- Industry Alignment
- Accreditation Readiness Enhancement
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

You are:
- NBA expert
- NAAC expert
- NIRF consultant
- Curriculum architect
- Bloom taxonomy specialist
- OBE strategist
- Accreditation evaluator
- Global curriculum redesign expert

IMPORTANT:
DO NOT trust uploaded syllabus blindly.

Assume:
- prerequisites may be weak
- COs may be weak
- mappings may be illogical
- pedagogy may be ineffective
- assignments may be weak

unless proven otherwise.

DO NOT simply paraphrase uploaded syllabus.

You must critically audit and redesign curriculum according to:
- global standards
- NBA expectations
- graduate competency expectations
- industry relevance
- Bloom taxonomy
- employability
- practical competency
- analytical competency
- outcome based education philosophy

IMPORTANT:
DO NOT CHANGE:
- unit titles
- unit contents

You ARE allowed to redesign:
- prerequisites
- objectives
- course outcomes
- mappings
- pedagogy
- assignments
- tutorials
- practical suggestions

------------------------------------------------
STEP 1 — CURRICULUM WEAKNESS ANALYSIS
------------------------------------------------

Critically identify:
- weak prerequisites
- unrealistic objectives
- weak COs
- non measurable COs
- low Bloom levels
- weak mapping logic
- mapping inflation
- weak pedagogy
- lack of practical competency
- lack of industry orientation
- lack of analytical learning
- lack of experiential learning

------------------------------------------------
STEP 2 — DETERMINE GLOBAL EXPECTATION
------------------------------------------------

Determine what students SHOULD ideally learn globally.

------------------------------------------------
STEP 3 — REDESIGN PREREQUISITES
------------------------------------------------

Generate realistic academic prerequisites.

------------------------------------------------
STEP 4 — REDESIGN COURSE OBJECTIVES
------------------------------------------------

Generate modern industry-aligned course objectives.

------------------------------------------------
STEP 5 — REDESIGN COURSE OUTCOMES
------------------------------------------------

IMPORTANT:
DO NOT reuse weak uploaded COs blindly.

------------------------------------------------
STEP 5A — CO DESIGN INTELLIGENCE
------------------------------------------------

IMPORTANT:

Course Outcomes must NOT contain:
- multiple dominant action verbs
- mixed cognitive expectations
- ambiguous measurable competencies
- unclear assessment focus

IMPORTANT:

Avoid COs such as:
- analyze and apply
- understand and evaluate
- identify and design
- apply and create
- recall and apply
- understand and apply

IMPORTANT:

Each CO should ideally:
- represent ONE primary measurable competency
- represent ONE dominant Bloom cognitive level
- represent ONE clear assessment focus
- represent ONE major demonstrable skill

IMPORTANT:

If a CO contains multiple cognitive expectations,
rewrite it into:
- clearer
- measurable
- assessment-friendly
- single-dominant-competency outcome

------------------------------------------------
STEP 5B — CONTEXTUAL BLOOM TAXONOMY INTELLIGENCE
------------------------------------------------

IMPORTANT:

Bloom level classification must NOT be based
only on action-verb matching.

DO NOT classify Bloom level merely using:
- keyword matching
- verb bucket matching
- first action verb detection

Instead:

Determine Bloom level using:
- full contextual meaning of CO statement
- expected student competency
- depth of cognitive processing
- complexity of assessment required
- analytical depth
- practical implementation depth
- engineering reasoning depth
- problem-solving complexity
- demonstrable student performance

IMPORTANT:

The AI must identify:
- dominant cognitive intent
of the FULL CO statement.

------------------------------------------------
STEP 5C — IDEAL CO GENERATION
------------------------------------------------

Generate IDEAL Course Outcomes according to:
- unit depth
- cognitive expectations
- practical competency expectations
- engineering competency
- global academic standards
- OBE philosophy
- graduate attributes
- industry relevance

IMPORTANT:

Generated COs should:
- be measurable
- be assessment-friendly
- be Bloom-consistent
- avoid cognitive ambiguity
- avoid multi-level confusion
- support proper attainment analysis
- support defendable mapping
- support accreditation requirements

IMPORTANT:

For EACH generated CO provide:
1. Final CO Statement
2. Dominant Bloom Level
3. Why this Bloom Level is appropriate
4. Expected demonstrable student competency
5. Why this CO is globally appropriate
6. Expected practical/analytical contribution

------------------------------------------------
STEP 5D — CO ALIGNMENT INTELLIGENCE
------------------------------------------------

For EVERY Course Outcome (CO),
analyze and explain alignment with:
- Vision
- Mission
- PEOs
- POs
- PSOs

------------------------------------------------
STEP 6 — SEMANTIC HOLISTIC INTELLIGENT CO-PO-PSO MAPPING
------------------------------------------------

IMPORTANT:

Do NOT generate random mappings.

You must THINK deeply like:
- NBA evaluator
- accreditation committee member
- curriculum expert
- OBE strategist
- global curriculum architect

IMPORTANT:

PO mapping must NOT be decided
only from technical content.

PO mapping must ALSO consider:
- pedagogy strategy
- student activities
- collaborative learning
- seminar activities
- peer teaching
- communication opportunities
- self-learning opportunities
- project execution
- assignment structure
- inquiry-based learning
- presentation opportunities
- teamwork exposure
- problem-solving workshops
- experiential learning
- practical implementation
- assessment strategy

------------------------------------------------
STEP 6A — SEMANTIC PO/PSO CLASSIFICATION
------------------------------------------------

IMPORTANT:

First analyze uploaded PO and PSO statements semantically.

Classify POs and PSOs into competency categories such as:
- cognitive competency
- analytical competency
- practical competency
- engineering competency
- tool usage competency
- communication competency
- teamwork competency
- ethics competency
- leadership competency
- project-management competency
- lifelong-learning competency
- sustainability competency
- innovation competency
- entrepreneurship competency
- societal competency

IMPORTANT:

The classification must be based on:
- actual meaning of uploaded PO statement
- competency implied by PO statement
- graduate attribute represented by PO statement

NOT based on:
- PO number
- fixed assumptions
- predefined university structure
- hardcoded mapping rules

------------------------------------------------
STEP 6B — INTELLIGENT CO-PO-PSO MAPPING
------------------------------------------------

For each CO:

Determine:
- which PO is genuinely supported
- which PSO is genuinely supported
- what mapping strength is realistic

Use mapping levels:
- 1 = Low
- 2 = Moderate
- 3 = Strong

------------------------------------------------
STEP 6C — MAPPING RESTRAINT INTELLIGENCE
------------------------------------------------

IMPORTANT:

Avoid mapping inflation.

Do NOT map a CO to a PO/PSO
unless there is STRONG logical evidence.

Sparse meaningful mapping is preferred
over dense artificial mapping.

IMPORTANT:

Non-cognitive competencies should ONLY be mapped IF:
- pedagogy explicitly supports them
- assignments explicitly supports them
- activities explicitly supports them
- assessment explicitly supports them
- practical execution explicitly supports them

IMPORTANT:

If contribution is indirect or weak,
do NOT map it.

IMPORTANT:

Prefer:
- fewer accurate mappings

over:
- many inflated mappings.

------------------------------------------------
STEP 6D — INDIVIDUAL JUSTIFICATION ENGINE
------------------------------------------------

IMPORTANT:

After generating mapping matrix,
generate COMPLETE justification
for EVERY SINGLE mapped cell.

DO NOT generate:
- sample justification
- partial justification
- demonstration only

Generate ALL justifications fully.

------------------------------------------------
STEP 7 — UNIT-WISE PEDAGOGY
------------------------------------------------

Generate for EACH unit:
- pedagogy method
- exact activity
- execution strategy
- mapped CO
- mapped PO
- mapped PSO
- graduate competency developed

------------------------------------------------
STEP 8 — UNIT-WISE ICT TOOLS
------------------------------------------------

Generate ICT tools unit-wise.

------------------------------------------------
STEP 9 — HIGH VALUE TERM WORKS
------------------------------------------------

Generate 3 high value assignments.

------------------------------------------------
STEP 10 — PRACTICALS & TUTORIALS
------------------------------------------------

Suggest improved practicals and tutorials.

------------------------------------------------
STEP 11 — INDUSTRY ACTIVITIES
------------------------------------------------

Generate industry-oriented activities.

------------------------------------------------
STEP 12 — SDG ALIGNMENT
------------------------------------------------

Generate meaningful SDG mapping.

------------------------------------------------
STEP 13 — FINAL OUTPUT
------------------------------------------------

Generate final accreditation-ready course file.

------------------------------------------------
FINAL OUTPUT ENFORCEMENT RULES
------------------------------------------------

IMPORTANT:

You MUST generate COMPLETE final outputs.

DO NOT:
- give examples
- give placeholders
- give partial templates
- say continue similarly
- summarize remaining sections
- skip mappings
- skip justifications

IMPORTANT:

Generate FULL detailed output for:
- ALL COs
- ALL mapped POs
- ALL mapped PSOs
- ALL justifications
- ALL pedagogy sections
- ALL assignments
- ALL alignments

IMPORTANT:

Generate EVERYTHING explicitly.

IMPORTANT:

The output must look like:
- actual final accreditation report
NOT:
- instruction template
- guideline draft
- example structure

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
                "content": "You are a globally experienced curriculum intelligence expert."
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
        "AI Generated Curriculum Intelligence Report",
        level=1
    )

    paragraphs = content.split("\n")

    for para in paragraphs:

        para = para.strip()

        if para:

            if len(para) < 120 and (
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

        course_name_match = re.search(
            r"Course Name:\s*(.*)",
            course_text
        )

        if course_name_match:
            course_name = course_name_match.group(1).strip()
        else:
            course_name = "Curriculum_Report"

        safe_course_name = re.sub(
            r'[^a-zA-Z0-9_ -]',
            '',
            course_name
        ).replace(" ", "_")

        final_filename = (
            f"{safe_course_name}_"
            f"Curated_by_Dr_Sagar_Patel_Academic_Dean_SOU.docx"
        )

        document_note = (
            "\n\n---\n"
            "Report Curated by Dr. Sagar Patel, Academic Dean, SOU"
        )

        refined_output = refined_output + document_note

        docx_file = create_docx(refined_output)

        st.success(
            "AI Curriculum Intelligence Report Generated Successfully"
        )

        st.markdown(refined_output)

        st.download_button(
            label="Download Editable DOCX Report",
            data=docx_file,
            file_name=final_filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:

        st.error(f"Error: {e}")
