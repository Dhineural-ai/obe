from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-4o-mini"
)


def analyze_alignment(vision_text, peo_text, course_text):

    prompt = PromptTemplate(
        input_variables=[
            "vision_text",
            "peo_text",
            "course_text"
        ],
        template="""
You are an NBA and OBE expert.

Analyze alignment between:

1. Vision and Mission
2. PEOs
3. POs and PSOs
4. Course Outcomes
5. Syllabus Topics
6. Teaching Methodology

Provide:

- Strong alignment areas
- Weak alignment areas
- Missing components
- Bloom taxonomy improvements
- Suggestions for improvement

VISION & MISSION:
{vision_text}

PEO/PO/PSO:
{peo_text}

COURSE FILE:
{course_text}
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "vision_text": vision_text,
        "peo_text": peo_text,
        "course_text": course_text
    })

    return response.content
