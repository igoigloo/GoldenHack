import openai

# Set the OpenAI API Key
openai.api_key = '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'

def get_business_idea(country):
    # Generate a business idea based on the country
    prompt = f"Generate a business idea for {country}"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )

    idea = response.choices[0].text.strip()
    return idea

# Example Usage
country = "India"
idea = get_business_idea(country)
print(f"Business idea for {country}: {idea}")