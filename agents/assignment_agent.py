from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_assignments(course_text):

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

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
