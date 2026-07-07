from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def marketing_agent(business_idea):

    prompt = f"""
You are a Marketing Director.

Business Idea:

{business_idea}

Create a professional marketing strategy.

Return ONLY:

# Brand Name

# Target Audience

# Branding Strategy

# Social Media Strategy

# Instagram Plan

# Facebook Plan

# SEO Strategy

# Advertisement Plan

# Budget

# Expected Results
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert marketing consultant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content