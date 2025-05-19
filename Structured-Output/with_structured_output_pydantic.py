from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional, Literal

load_dotenv()

model = ChatOpenAI()

#schema  
class Review(TypedDict):
    key_themes : Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    summary : Annotated[str,"A Brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"],"Return sentiment of the review either negative, positive or neutral"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name: Annotated[Optional[str],"Write the name of the reviewer"]

    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """This is the best laptop under the price range i got and has best feature with latest Graffic card that i really loved the performance of laptop but it has a small issue of battery but it is justifyable becuase it has a graffic card"""
)

print(result)
