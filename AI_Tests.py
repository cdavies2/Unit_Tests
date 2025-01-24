import os
from openai import OpenAI 

client1=OpenAI(
    api_key=os.environ.get("GLHF_API_KEY"),
    base_url="https://glhf.chat/api/openai/v1",
)

#first we'll access the models via GLHF

# misModel=client1.chat.completions.create(
#     model="hf:mistralai/Mistral-7B-Instruct-v0.3",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Explain what a prompt injection is"}
#     ]
# )
# print("This is our response from the Mistralai model: ")
# print(misModel.choices[0].message.content) #message.content makes it so we'll only see the actual response, no other data

llaModel=client1.chat.completions.create(
    model="hf:meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Explain what a prompt injection is"}
    ]
)

print("This is out response from the Llama3 model: ")
print(llaModel.choices[0].message.content)

#now let's access gpt-4 via OpenAI


# Unit Test 1: Getting a Text Response from various models

# One Test for an OpenAI GPT, one for Llama3 and one for Mistral

# Unit Test 2: Checking the Text Response for specific content

# Unit Test 3: Modifying the system prompt, documenting change in output
# For this one, get the output outside of the teststringmethods class so you can more clearly observe/document changes
# Once you've determined which prompts are most helpful in getting what you want, test those for specific content

# Unit Test 4: Code Generation from each model and running the code

# Unit Test 5: Try the trivial LLama3 Jailbreak from the GitHub below
# https://github.com/haizelabs/llama3-jailbreak/blob/master/trivial.py