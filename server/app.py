import os
from groq import Groq

# Initialize global variables
client = None
GROQ_API_KEY = None
model_name = None

# Function to set API key
def set_api_key(api_key):
    global GROQ_API_KEY, client
    GROQ_API_KEY = api_key
    client = Groq(api_key=GROQ_API_KEY)
    print(f"API Key set: {GROQ_API_KEY}")

# Function to set model
def set_model(model):
    global model_name
    model_name = model
    print(f"Model set: {model_name}")

# Function to convert code
def convert_code(input_code, input_lang, output_lang):
    prompt = f"Give only the code without any explanation, comments or any '''. Only just the raw code. Convert this {input_code} in {input_lang} code into {output_lang}."
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model_name,
        )
        print("Translation process done")
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True)

