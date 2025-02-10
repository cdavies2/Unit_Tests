import os, pytest
from openai import OpenAI 
import unittest

client1=OpenAI(
    api_key=os.environ.get("GLHF_API_KEY"),
    base_url="https://glhf.chat/api/openai/v1",
)

def make_model(modelType, message, convo=None):
    #convo originally equals None because this parameter will not always be filled
    if convo==None: #this is when the model is initially built, no context is sent to it
        prompts=[{"role": "system", "content": """You are a helpful assistant, if I asked you something 
        you cannot help me with, please respond 'I am sorry, I cannot answer that ' """},
              {"role": "user", "content": message}] #the starting messages are saved outside the ChatCompletion object
        testModel=client1.chat.completions.create(
            model=modelType,
            messages=prompts #the initial prompts comprise the messages sent to the model
            )
    else: #context is being sent to the model
        prompts=convo
        prompts.append({"role": "user", "content": message}) #the new message is added to the array after the context
        testModel=client1.chat.completions.create(
                model=modelType, #modelType is consistent
                messages=prompts
                )
    prompts.append({"role": "assistant", "content": testModel.choices[0].message.content})
    #the model's response to the user is added to the array
    return testModel, prompts #both the model and the array of messages are returned

mistral="hf:mistralai/Mistral-7B-Instruct-v0.3"
llama="hf:meta-llama/Llama-3.3-70B-Instruct"

models=[mistral, llama]

class TestStringMethods(unittest.TestCase):
# Unit Test 1: Getting a Text Response from various models
# try testing with both models using subtests
    def test_returns(self):
        for i in models:
            with self.subTest(i=i):
                testMessage="This is a test, only say 'hello'"
                tMod, context1=make_model(i, testMessage) #tmod contains the model itself, context contains the messages
                self.assertTrue(tMod!="")


@pytest.mark.parametrize("model", [(mistral), (llama)]) #this uses pytest's parametrize function to run the tests with both models
def test_return2(model):
    testMessage="This is a test, only say 'hello'"
    tMod, context1=make_model(model, testMessage)
    assert tMod!=""