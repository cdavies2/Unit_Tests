import os
from openai import OpenAI 
import unittest

# client1=OpenAI(
#     api_key=os.environ.get("GLHF_API_KEY"),
#     base_url="https://glhf.chat/api/openai/v1",
# )

# #first we'll access the models via GLHF

# # misModel=client1.chat.completions.create(
# #     model="hf:mistralai/Mistral-7B-Instruct-v0.3",
# #     messages=[
# #         {"role": "system", "content": "You are a helpful assistant."},
# #         {"role": "user", "content": "Explain what a prompt injection is"}
# #     ]
# # )
# # print("This is our response from the Mistralai model: ")
# # print(misModel.choices[0].message.content) #message.content makes it so we'll only see the actual response, no other data



# # llaModel=client1.chat.completions.create(
# #     model="hf:meta-llama/Llama-3.3-70B-Instruct",
# #     messages=[
# #         {"role": "system", "content": "You are a helpful assistant"},
# #         {"role": "user", "content": "Explain what a unit test is"}
# #     ]
# # )

# # print("This is out response from the Llama3 model: ")
# # print(llaModel.choices[0].message.content)

# #now let's access gpt-4 via OpenAI



# # The method below will be used in the unit tests, it will create models/messages as we need them
# #modify this later to account for the gpt model
# def make_model(modelType, message):
#     testModel=client1.chat.completions.create(
#          model=modelType,
#          messages=[
#               {"role": "system", "content": "You are a helpful assistant"},
#               {"role": "user", "content": message}
#               ]
#               )
#     return testModel




# # Unit Test 1: Getting a Text Response from various models


# # One Test for an OpenAI GPT, one for Llama3 and one for Mistral
# class TestStringMethods(unittest.TestCase):
#     def test_returns(self):
#         testMessage="This is a test, only say 'hello'"
#         tMod1=make_model("hf:mistralai/Mistral-7B-Instruct-v0.3", testMessage)
#         tMod2=make_model("hf:meta-llama/Llama-3.3-70B-Instruct", testMessage)
#         tString=tMod1.choices[0].message.content
#         self.assertTrue(tString!="")
#         tString=tMod2.choices[0].message.content
#         self.assertTrue(tString!="")

# # Unit Test 2: Checking the Text Response for specific content
#     def test_content(self):
#         testMessage="Please explain what a prompt injection is, and use the word 'vulnerability' in your explanation"
#         tMod1=make_model("hf:mistralai/Mistral-7B-Instruct-v0.3", testMessage)
#         tMod2=make_model("hf:meta-llama/Llama-3.3-70B-Instruct", testMessage)
#         tString=tMod1.choices[0].message.content
#         self.assertIn("vulnerability", tString)
#         tString=tMod2.choices[0].message.content
#         self.assertTrue("vulnerability", tString)

# # Unit Test 3: Modifying the system prompt, documenting change in output
# # For this one, get the output outside of the teststringmethods class so you can more clearly observe/document changes
# # Once you've determined which prompts are most helpful in getting what you want, test those for specific content

# # Unit Test 4: Code Generation from each model and running the code


# # Unit Test 5: Evaluating Models Using the Tests they Produced


# # Unit Test 6: Try the trivial LLama3 Jailbreak from the GitHub below
# # https://github.com/haizelabs/llama3-jailbreak/blob/master/trivial.py
# if __name__ == '__main__':
#     unittest.main()