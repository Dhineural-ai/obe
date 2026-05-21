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

IMPORTANT:
DO NOT trust uploaded syllabus blindly.

Assume:
- prerequisites may be weak
- COs may be weak
- mappings may be illogical
- pedagogy may be ineffective

unless proven otherwise.

DO NOT simply paraphrase.

You must critically audit and redesign curriculum according to:
- global standards
- NBA expectations
- graduate competency expectations
- industry relevance
- Bloom taxonomy
- employability
- practical competency

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

STEP 1:
Analyze weaknesses in current syllabus.

STEP 2:
Determine what students SHOULD ideally learn globally.

STEP 3:
Redesign prerequisites logically.

STEP 4:
Redesign course objectives intelligently.

------------------------------------------------
STEP 5 — REDESIGN COURSE OUTCOMES
------------------------------------------------

IMPORTANT:

DO NOT reuse weak uploaded COs blindly.

Critically evaluate existing COs and redesign them according to:
- global curriculum standards
- NBA expectations
- Bloom taxonomy
- graduate competency expectations
- industry expectations
- practical competency
- analytical competency
- employability requirements
- measurable assessment expectations

------------------------------------------------

STEP 5A — CO DESIGN INTELLIGENCE

IMPORTANT:

Course Outcomes must NOT contain:
- multiple dominant action verbs
- mixed cognitive expectations
- ambiguous measurable competencies
- unclear assessment focus

IMPORTANT:

Avoid COs such as:
- "analyze and apply"
- "understand and evaluate"
- "identify and design"
- "apply and create"

unless one competency is clearly dominant.

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

NOT merely:
- action verbs
- Bloom keyword lists

------------------------------------------------

STEP 5C — IDEAL CO GENERATION

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

IMPORTANT:

For EVERY Course Outcome (CO),
analyze and explain alignment with:
- Vision
- Mission
- PEOs
- POs
- PSOs

IMPORTANT:

Do NOT generate generic statements.

For EACH CO explain:
1. HOW the CO contributes to institutional Vision
2. HOW the CO supports institutional Mission
3. HOW the CO contributes to specific PEOs
4. HOW the CO supports specific POs
5. HOW the CO supports specific PSOs

IMPORTANT:

The explanation must include:
- cognitive contribution
- analytical contribution
- employability contribution
- practical competency contribution
- innovation contribution
- teamwork contribution
- communication contribution
- engineering contribution
- problem-solving contribution

FORMAT STRICTLY LIKE THIS:

ALIGNMENT OF CO1 WITH VISION:
Explain clearly.

ALIGNMENT OF CO1 WITH MISSION:
Explain clearly.

ALIGNMENT OF CO1 WITH PEO1:
Explain clearly.

ALIGNMENT OF CO1 WITH PO1:
Explain clearly.

ALIGNMENT OF CO1 WITH PSO1:
Explain clearly.

IMPORTANT:

Do this for ALL COs.

The explanation must be:
- accreditation ready
- academically meaningful
- logically defendable
- competency based
- outcome based
- globally aligned

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

For each CO:

Determine:
- which PO is genuinely supported
- which PSO is genuinely supported
- what mapping strength is realistic

Use mapping levels:
- 1 = Low
- 2 = Moderate
- 3 = Strong

IMPORTANT:

Mapping strength must be based on:
- actual competency contribution
- Bloom level
- practical exposure
- analytical depth
- communication exposure
- teamwork exposure
- tool usage
- problem solving
- real-world application
- self-learning exposure
- presentation exposure
- collaborative learning exposure
- inquiry-based learning exposure
- assessment evidence
- assignment evidence
- pedagogy evidence

------------------------------------------------

STEP 6C — MAPPING RESTRAINT INTELLIGENCE

IMPORTANT:

Avoid mapping inflation.

Do NOT map a CO to a PO/PSO
unless there is STRONG logical evidence.

Sparse meaningful mapping is preferred
over dense artificial mapping.

IMPORTANT:

Non-cognitive competencies such as:
- communication
- teamwork
- ethics
- leadership
- project management
- lifelong learning
- sustainability

should ONLY be mapped IF:
- pedagogy explicitly supports them
- assignments explicitly support them
- activities explicitly support them
- assessment explicitly supports them
- practical execution explicitly supports them

IMPORTANT:

If contribution is indirect or weak,
do NOT map it.

Mapping should reflect:
- genuine measurable contribution
- observable competency development
- defendable accreditation logic
- realistic student competency attainment

IMPORTANT:

Prefer:
- fewer accurate mappings

over:
- many inflated mappings.

A mapping should only exist if:
students genuinely demonstrate
that competency through:
- learning activities
- assessment
- assignments
- pedagogy
- practical execution
- collaborative engagement
- presentations
- inquiry activities

------------------------------------------------

STEP 6D — INDIVIDUAL JUSTIFICATION ENGINE

VERY IMPORTANT:

After generating mapping matrix,
generate INDIVIDUAL JUSTIFICATION
for EVERY SINGLE mapping value.

FORMAT STRICTLY LIKE THIS:

MAPPING OF CO1 TO PO1 (VALUE 3):
Explain:
- WHY this mapping exists
- HOW CO1 contributes to PO1
- WHY contribution strength is STRONG
- Which competency dimensions support this mapping
- Which Bloom level supports this mapping
- Which pedagogy/assessment/activity supports this mapping

MAPPING OF CO1 TO PO9 (VALUE 2):
Explain:
- HOW collaborative pedagogy supports teamwork
- HOW group analytical activities support this competency
- WHY teamwork contribution is MODERATE

MAPPING OF CO1 TO PO10 (VALUE 1):
Explain:
- HOW presentation/discussion/self-expression
supports communication competency
- WHY communication contribution is LOW

IMPORTANT:

DO THIS FOR:
- EVERY CO
- EVERY mapped PO
- EVERY mapped PSO

The justification must NOT be generic.

Each justification must be:
- competency-specific
- Bloom-specific
- logically defendable
- accreditation-ready
- academically meaningful
- pedagogy-aware
- assessment-aware

The explanation must clearly show:
- cognitive contribution
- analytical contribution
- practical contribution
- communication contribution
- teamwork contribution
- tool contribution
- engineering contribution
- real-world application contribution
- lifelong learning contribution
- leadership contribution
- project management contribution

IMPORTANT:

The justification should be detailed enough
that an accreditation evaluator can clearly understand:
WHY the mapping value is logically correct.

STEP 6 — SEMANTIC HOLISTIC INTELLIGENT CO-PO-PSO MAPPING

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

For each CO:

Determine:
- which PO is genuinely supported
- which PSO is genuinely supported
- what mapping strength is realistic

Use mapping levels:
- 1 = Low
- 2 = Moderate
- 3 = Strong

IMPORTANT:

Mapping strength must be based on:
- actual competency contribution
- Bloom level
- practical exposure
- analytical depth
- communication exposure
- teamwork exposure
- tool usage
- problem solving
- real-world application
- self-learning exposure
- presentation exposure
- collaborative learning exposure
- inquiry-based learning exposure
- assessment evidence
- assignment evidence
- pedagogy evidence

------------------------------------------------

STEP 6C — MAPPING RESTRAINT INTELLIGENCE

IMPORTANT:

Avoid mapping inflation.

Do NOT map a CO to a PO/PSO
unless there is STRONG logical evidence.

Sparse meaningful mapping is preferred
over dense artificial mapping.

IMPORTANT:

Non-cognitive competencies such as:
- communication
- teamwork
- ethics
- leadership
- project management
- lifelong learning
- sustainability

should ONLY be mapped IF:
- pedagogy explicitly supports them
- assignments explicitly support them
- activities explicitly support them
- assessment explicitly supports them
- practical execution explicitly supports them

IMPORTANT:

If contribution is indirect or weak,
do NOT map it.

Mapping should reflect:
- genuine measurable contribution
- observable competency development
- defendable accreditation logic
- realistic student competency attainment

IMPORTANT:

Prefer:
- fewer accurate mappings

over:
- many inflated mappings.

A mapping should only exist if:
students genuinely demonstrate
that competency through:
- learning activities
- assessment
- assignments
- pedagogy
- practical execution
- collaborative engagement
- presentations
- inquiry activities

------------------------------------------------

STEP 6D — INDIVIDUAL JUSTIFICATION ENGINE

VERY IMPORTANT:

After generating mapping matrix,
generate INDIVIDUAL JUSTIFICATION
for EVERY SINGLE mapping value.

FORMAT STRICTLY LIKE THIS:

MAPPING OF CO1 TO PO1 (VALUE 3):
Explain:
- WHY this mapping exists
- HOW CO1 contributes to PO1
- WHY contribution strength is STRONG
- Which competency dimensions support this mapping
- Which Bloom level supports this mapping
- Which pedagogy/assessment/activity supports this mapping

MAPPING OF CO1 TO PO9 (VALUE 2):
Explain:
- HOW collaborative pedagogy supports teamwork
- HOW group analytical activities support this competency
- WHY teamwork contribution is MODERATE

MAPPING OF CO1 TO PO10 (VALUE 1):
Explain:
- HOW presentation/discussion/self-expression
supports communication competency
- WHY communication contribution is LOW

IMPORTANT:

DO THIS FOR:
- EVERY CO
- EVERY mapped PO
- EVERY mapped PSO

The justification must NOT be generic.

Each justification must be:
- competency-specific
- Bloom-specific
- logically defendable
- accreditation-ready
- academically meaningful
- pedagogy-aware
- assessment-aware

The explanation must clearly show:
- cognitive contribution
- analytical contribution
- practical contribution
- communication contribution
- teamwork contribution
- tool contribution
- engineering contribution
- real-world application contribution
- lifelong learning contribution
- leadership contribution
- project management contribution

IMPORTANT:

The justification should be detailed enough
that an accreditation evaluator can clearly understand:
WHY the mapping value is logically correct.

STEP 7:
Generate UNIT-WISE pedagogy.

For each unit:
- pedagogy method
- exact activity
- how activity should be conducted
- mapped CO
- mapped PO
- mapped PSO
- graduate competency developed

Use:
- Inquiry Based Learning
- Peer Teaching
- Group Learning
- Problem Solving
- Technology Based Learning
- Game Based Learning
- Collaborative Learning
- Any other Student Centric Teaching Learning Activities 
STEP 8:
Generate UNIT-WISE ICT tools.

STEP 9:
Generate 3 HIGH VALUE TERM WORKS.

Assignments must:
- cover all units
- support CO attainment
- support PO attainment
- improve employability
- improve communication
- improve teamwork
- improve practical competency

For each assignment provide:
- title
- objective
- execution strategy
- mapped COs
- mapped POs
- mapped PSOs
- Bloom level

STEP 10:
Suggest improved practicals and tutorials.

STEP 11:
Generate industry-oriented activities.

STEP 12:
Generate SDG mapping.

STEP 13:
Generate final modern accreditation-ready course file.

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
