
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables first
load_dotenv(override=True)

HF_TOKEN = os.getenv("HF_A_TOKEN")

client = AsyncOpenAI(base_url="https://router.huggingface.co/v1", api_key=HF_TOKEN)

MODEL = os.getenv("HF_MODEL", "openai/gpt-oss-20b:fastest")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN is not configured")

async def generate_research_plan(
    question: str, context: str = "") -> str:

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
