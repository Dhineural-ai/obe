from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    temperature=0.4,
    model="gpt-4o-mini"
)


def refine_course_document(
    vision_text,
    peo_text,
    course_text
):

    prompt = PromptTemplate(
        input_variables=[
            "vision_text",
            "peo_text",
            "course_text"
        ],
        template="""
You are a senior Dean Academics and NBA expert.

Your task is to generate a refined and upgraded version of the uploaded course file.

Improve:

1. Course Outcomes
2. Bloom taxonomy alignment
3. CO-PO Mapping
4. Course Objectives
5. Teaching methodology
6. ICT tools
7. Assessment strategy
8. Laboratory activities
9. Mini-project suggestions
10. Experiential learning activities
11. Value-added content
12. Employability alignment
13. Skill development focus
14. Modern industry relevance
15. AI integration opportunities

The final document should look like a professionally redesigned NBA-oriented syllabus.

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
