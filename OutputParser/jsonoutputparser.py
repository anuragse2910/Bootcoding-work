from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template= " Give me the name, age adn city of a fictional person\n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    
)

# prompt = template.format()

# result = model.invoke(prompt)

# print(result)

# final_result = parser.parse(result.content)
"""this is the alternatative of above code"""
chain = template | model | parser
result = chain.invoke({})

print(result) 