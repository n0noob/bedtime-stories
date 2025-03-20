from collections import namedtuple
from typing import List
from openai import OpenAI

Response = namedtuple("Response", ["output_text"])

class OpenAIAdapter:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def get_me_a_story(self, attributes: List[str] = None) -> str:
        request_line = "Tell me a story"
        if attributes:
            request_line += f" with these attributes: {attributes}"
        print(f"Input line: {request_line}")
        # response = self.client.responses.create(
        #     model="gpt-4o",
        #     instructions="You are a husband who is telling a bedtime story to your wife to make her fall asleep",
        #     input=request_line,
        # )
        response = Response("Hello, this is the output text!")
        return response.output_text