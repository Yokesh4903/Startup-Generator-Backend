from services.openai_service import generate_response

response = generate_response(
    "You are a startup expert.",
    "Launch a bakery in Chennai."
)

print(response)