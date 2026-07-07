from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def hr_agent(business_idea):

    prompt = f"""
You are an HR Manager.

Business Idea:

{business_idea}

Return ONLY:

# Team Structure

# Hiring Plan

# Employee Roles

# Recruitment Strategy

# Salary Estimate

# Company Culture

# HR Policies
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an HR expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content