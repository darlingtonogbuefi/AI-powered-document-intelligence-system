# \test_valid_prompt.py

from bedrock_utils import valid_prompt

# Replace with your actual model ID
model_id = "anthropic.claude-3-5-haiku-20241022-v1:0"

# Sample user prompt to test
user_input = "How does this AI model work internally?"

# Test the function
is_valid = valid_prompt(user_input, model_id)

print(f"Is prompt valid? {is_valid}")
