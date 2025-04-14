#Code-test generator
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from config import OPENAI_BASE_URL
from dotenv import load_dotenv
import argparse

#For loading out api secretly
load_dotenv()

#For allowing terminal manipulation to certain inputs like 'task' and 'language'
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

#Basic Configuration
deployment_name = "gpt-4o-mini-tds"
openai_api_version = "2024-08-01-preview"
openai_api_type = "azure"

#Setting up LLM(GPT)
llm = AzureChatOpenAI(
        azure_endpoint = OPENAI_BASE_URL,
        openai_api_version = openai_api_version,
        deployment_name = deployment_name,
        openai_api_type = openai_api_type
    )

#1st Part
code_prompt = PromptTemplate(
        input_variables=["language","task"],
        template = "Write a very short {language} function that will {task}", #Placeholders taken as variable due to the properties of library  
    )
#Use pipe operator to make code chain
code_chain = code_prompt | llm
generated_code = code_chain.invoke({
    "language": args.language,
    "task": args.task
    })
print("Generated Code:",generated_code.content)

#2nd Part
test_prompt = PromptTemplate(
        input_variables=["language","code"],
        template = "Write a test for the following {language} code: \n{code}", #Placeholders taken as variable due to the properties of library  
    )
#Using ouput code of first chain in 2nd chain = Sequential Chaining (ca also be achieved by using 'SequentialChain' Class)
test_chain = test_prompt | llm
generated_test = test_chain.invoke({
    "language": args.language,
    "code": generated_code
    })
print(generated_test.content)

