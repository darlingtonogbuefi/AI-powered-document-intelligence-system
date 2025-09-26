## \test_chatbot.py

from bedrock_utils import query_knowledge_base, generate_response, valid_prompt

# Test data
test_prompt = "What safety features are built into the FL250 forklift according to its spec sheet?"
test_model_id = "anthropic.claude-3-5-haiku-20241022-v1:0"  # or your chosen model
test_kb_id = "J6X0E7YNBF"

# Test valid_prompt
is_valid = valid_prompt(test_prompt, test_model_id)
print("valid_prompt output:", is_valid)

# Test query_knowledge_base
kb_results = query_knowledge_base(test_prompt, test_kb_id)
print("query_knowledge_base output:", kb_results)

# Test generate_response
if is_valid:
    context = "\n".join([result['content']['text'] for result in kb_results])
    full_prompt = f"Context: {context}\n\nUser: {test_prompt}\n\n"
    response = generate_response(full_prompt, test_model_id, temperature=1, top_p=1)
    print("generate_response output:", response)
else:
    print("Prompt not valid, skipping generate_response.")
