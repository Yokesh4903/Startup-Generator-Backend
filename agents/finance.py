from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def finance_agent(business_idea):

    prompt = f"""
You are a Financial Advisor.

Business Idea:

{business_idea}

Return ONLY:

# Startup Cost

# Monthly Expenses

# Revenue Estimate

# Profit Estimate

# Break-even Analysis

# Investment Needed

# Financial Risks
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a startup finance expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content