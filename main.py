import ollama
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from prompts import *

# 1. local Ollama for evaluating if loading safety is given or not


script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
image = os.path.join(script_dir, "input", "loading1.jpg") 

prompt_message = "Describe very briefly if you think the loading safety of this vehicle is okay or not."

response = ollama.chat(
    model= "llava:7b",
    messages= [
        {"role": "user",
         "content": prompt_message,
         "images": [image]}
    ]
)

ollama_evaluation = response["message"]["content"]
print("\nAssistant Ollama Evaluation: \n\n")
print(ollama_evaluation)


script_dir = os.path.dirname(os.path.abspath(__file__)) 
assistant_ollama_path = os.path.join(script_dir, "output", "Assistant_Ollama.txt") 

with open(assistant_ollama_path, "w") as file:
    file.write(ollama_evaluation)



# 2. OpenAI API to process evaluation of ollama and create potential warnings

# load the .env file
_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

# initialize model settings
model = "gpt-4o"
temperature = 0.3
max_tokens = 800
    
# prompts variables for first assistant
system_message = system_message
prompt = generate_prompt(ollama_evaluation)


# assistant function to execute model with prompt
def shipment_information_assistant():
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {   
                "role": "system", 
                "content": system_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content

result = shipment_information_assistant()
print("\nAssistant OpenAI potential warning: \n\n")
print(result)

# saving potential warning as a textfile

script_dir = os.path.dirname(os.path.abspath(__file__))
potential_warning_path = os.path.join(script_dir, "output", "Assistant_OpenAI.txt") 

with open(potential_warning_path, "w") as file:
    file.write(result)