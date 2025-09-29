# \test_valid_prompt.py

import os
from dotenv import load_dotenv
from bedrock_utils import valid_prompt

# Load environment variables
load_dotenv()

# Get model ID from .env
model_id = os.getenv("MODEL_ID_35")  # or MODEL_ID_37 depending on what you want to test

# Sample user prompt to test
user_input = "How does this AI model work internally?"

# Test the function
is_valid = valid_prompt(user_input, model_id)

print(f"Is prompt valid? {is_valid}")
