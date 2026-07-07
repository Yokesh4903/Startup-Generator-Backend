from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def sales_agent(business_idea):

    prompt = f"""
You are a Sales Director.

Business Idea:

{business_idea}

Return ONLY:

# Pricing Strategy

# Sales Channels

# Monthly Sales Forecast

# Customer Acquisition

# Sales Targets

# Revenue Projection

# Upselling Strategy
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a sales expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content