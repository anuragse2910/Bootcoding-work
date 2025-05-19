from click import prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

# 1st Prompt -> detailed report
template1 = PromptTemplate(
    template="write a deatiled report {topic}",
    input_variables=["topic"]
)
# 2nd Prompt -> summary
template2 = PromptTemplate(
    template="write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic':'blackchole'})
result = model.invoke(prompt)

prompt2 = template2.invoke({'text':result.content})
result2 = model.invoke(prompt2)

print(result2)