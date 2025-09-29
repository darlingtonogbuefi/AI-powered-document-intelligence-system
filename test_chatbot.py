## \test_chatbot.py

import os
from dotenv import load_dotenv
from bedrock_utils import query_knowledge_base, generate_response, valid_prompt

# Load environment variables
load_dotenv()

# Test data
test_prompt = "What safety features are built into the FL250 forklift according to its spec sheet?"
test_model_id = os.getenv("MODEL_ID_35")  # from .env
kb_id = os.getenv("KB_ID")                 # from .env

print(f"Testing with model_id={test_model_id} and kb_id={kb_id}")

# Test valid_prompt
is_valid = valid_prompt(test_prompt, test_model_id)
print("valid_prompt output:", is_valid)

# Test query_knowledge_base
kb_results = query_knowledge_base(test_prompt, kb_id)

print("Example KB Result:")
if kb_results:
    import pprint
    pprint.pprint(kb_results[0])
else:
    print("No KB results found.")

# Continue with your existing generate_response test if desired
if is_valid and kb_results:
    context = "\n".join([result['content']['text'] for result in kb_results])
    full_prompt = f"Context: {context}\n\nUser: {test_prompt}\n\n"
    response = generate_response(full_prompt, test_model_id, temperature=1, top_p=1)

    # Extract sources for demo print
    sources = set()
    for result in kb_results:
        source = result.get('location', {}).get('s3Location', {}).get('uri')
        if source:
            sources.add(source)

    # Append sources to response (optional for testing)
    if sources:
        source_text = "\n\n---\n**Sources:**\n" + "\n".join(f"- {src}" for src in sources)
        response += source_text

    print("generate_response output:", response)
else:
    print("Prompt not valid or no KB results, skipping generate_response.")
