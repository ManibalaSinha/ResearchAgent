
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables first
load_dotenv(override=True)

API_KEY = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(api_key=API_KEY)

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

async def generate_research_plan(
    question: str, context: str = "") -> str:

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured")

    prompt = f"""
    You are an expert AI research assistant.

    Research question:
    {question}

    Additional context:
    {context or "No additional context provided."}

    Create a structured research plan containing:

    1. Research objective
    2. Key research questions
    3. Important subtopics
    4. Search keywords
    5. Research methodology
    6. Expected findings
    7. Potential limitations

    Do not invent research findings or sources.
    Clearly distinguish hypotheses from verified facts.
    """

    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional research planning assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content or ""
