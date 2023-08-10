from typing import List
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_interest: str = Field(description="A topic that may interest the person")
    ice_breakers: List[str] = Field(description="Ice breakers to start a conversation with the person")

    def to_dict(self):
        return {"summary": self.summary, "facts": self.facts, "topics_interest": self.topics_interest,
                "ice_breakers": self.ice_breakers}


person_intel_parser = PydanticOutputParser(pydantic_object=PersonIntel)
