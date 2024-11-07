import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class TamilAI:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def get_response(self, question: str) -> str:
        """Get response from OpenAI API in Tamil"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that always responds in Tamil language. "
                                 "Provide responses with proper Tamil grammar and script."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error: {str(e)}" 