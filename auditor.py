import os
import openai
import json
import time

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables. Please set it before running.")

openai.api_key = OPENAI_API_KEY

def evaluate_privacy_risks(system_name: str, data_fields: list, purpose: str) -> dict:
    prompt = f"""
    System: {system_name}
    Purpose: {purpose}
    Data Fields: {', '.join(data_fields)}

    Please assess potential privacy risks under GDPR and EU AI Act principles.

    Return in JSON format:
    {{
        "risk_areas": [...],
        "risk_level": "High/Medium/Low",
        "suggested_actions": [...]
    }}
    """

    for attempt in range(3):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": "You are a compliance and privacy advisor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            raw_output = response['choices'][0]['message']['content'].strip()
            try:
                return json.loads(raw_output)
            except json.JSONDecodeError:
                return {"raw_response": raw_output}
        except openai.error.OpenAIError as e:
            print(f"OpenAI API Error: {str(e)}")
            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                return {"error": str(e)}
