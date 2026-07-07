from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def generate_response(system_prompt, user_prompt):
    """
    Sends a request to GPT-4o mini and returns the response text.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content