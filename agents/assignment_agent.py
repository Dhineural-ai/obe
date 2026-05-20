from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def generate_assignments(course_text):

    prompt = f'''
Generate:
- Unit-wise assignments
- Problem-solving activities
- Mini projects
- Student-centric learning activities

Based on:
{course_text}
'''

    response = llm.invoke(prompt)

    return response.content
