from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def ceo_agent(business_idea):

    prompt = f"""
You are an experienced Startup CEO.

Create a professional business strategy for:

Business Idea:
{business_idea}

Return ONLY in this format.

# Business Name

# Vision

# Mission

# Business Model

# Target Customers

# Revenue Model

# Growth Strategy

# Competitive Advantage

# Risks

# Future Expansion

Keep every section concise and professional.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert startup CEO."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content