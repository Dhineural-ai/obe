from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    temperature=0.2,
    model="gpt-4o-mini"
)


def generate_mapping_analysis(course_text, peo_text):

    prompt = PromptTemplate(
        input_variables=[
            "course_text",
            "peo_text"
        ],
        template="""
You are an NBA accreditation expert.

Analyze the CO-PO-PSO mapping quality.

Provide:

1. Existing mapping issues
2. Missing mapping relationships
3. Suggested CO improvements
4. Bloom taxonomy corrections
5. Better action verbs
6. Suggested attainment strategy
7. Suggested rubrics

PEO/PO/PSO DATA:
{peo_text}

COURSE FILE:
{course_text}
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "course_text": course_text,
        "peo_text": peo_text
    })

    return response.content
