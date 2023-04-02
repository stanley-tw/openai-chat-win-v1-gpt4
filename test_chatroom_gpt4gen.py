import os
import unittest
from io import StringIO
from unittest.mock import patch
from chatroom_gpt4gen import generate_response
from dotenv import load_dotenv

# Configure the OpenAI API key
load_dotenv()

class TestChatApp(unittest.TestCase):
    def setUp(self):
        self.original_api_key = os.environ.get("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = "your_test_api_key"

    def tearDown(self):
        if self.original_api_key:
            os.environ["OPENAI_API_KEY"] = self.original_api_key
        else:
            del os.environ["OPENAI_API_KEY"]

    def test_generate_response(self):
        messages = [
            {"role": "system", "content": "Chat with the AI"},
            {"role": "user", "content": "What is the capital of France?"}
        ]
        response = generate_response(messages)
        self.assertIn("Paris", response)

    def test_clear_history(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            messages = [
                {"role": "system", "content": "Chat with the AI"},
                {"role": "user", "content": "/clear"}
            ]
            response = generate_response(messages)
            self.assertNotIn("Chat with the AI", response)

if __name__ == '__main__':
    unittest.main()
