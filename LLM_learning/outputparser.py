from typing import List, Dict, Any
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

# Define your Pydantic model for Summary
class Summary(BaseModel):
    summary: str = Field(description="Provide a summary of the person's profile.")
    facts: List[str] = Field(description="Provide interesting facts about them.")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}


# Create the parser
summary_parser = PydanticOutputParser(pydantic_object=Summary)

# Manually define the format instructions
def get_summary_format_instructions() -> str:
    return """
    The output should be a JSON object with the following structure:
    {
        "summary": "Provide a summary of the person's profile as a string.",
        "facts": "Provide a list of interesting facts about the person."
    }
    """

