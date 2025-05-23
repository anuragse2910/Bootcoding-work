from ast import parse
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = 'fact_1', description="Fact 1 about the topic"),
    ResponseSchema(name = 'fact_2', description="Fact 2 about the topic"),
    ResponseSchema(name = 'fact_3', description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template = "given 3 fact about the {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables= {'format_instruction':parse.get_format_instruction()}
)

chain = template | model | parser

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)
result = chain.invoke({'topic':'black hole'})
print(result)

# final_result = parser.parse(result.content)
# print(final_result)