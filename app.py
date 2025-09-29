# \app.py

import os
import streamlit as st
from dotenv import load_dotenv
from bedrock_utils import query_knowledge_base, generate_response, valid_prompt

# Load environment variables from .env file
load_dotenv()

# Streamlit UI
st.title("Chat Application")

# Sidebar for configurations
st.sidebar.header("Configuration")

# Mapping friendly model names to environment variables
model_choices = {
    "Claude 3.5 Haiku": os.getenv("MODEL_ID_35"),
    "Claude 3.7 Sonnet": os.getenv("MODEL_ID_37")
}

selected_label = st.sidebar.selectbox("Select LLM Model", list(model_choices.keys()))
model_id = model_choices[selected_label]

# Knowledge Base ID is loaded from env and NOT exposed to UI
kb_id = os.getenv("KB_ID")

temperature = st.sidebar.select_slider("Temperature", [i / 10 for i in range(0, 11)], 1)
top_p = st.sidebar.select_slider("Top_P", [i / 1000 for i in range(0, 1001)], 1)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if valid_prompt(prompt, model_id):
        # Query Knowledge Base
        kb_results = query_knowledge_base(prompt, kb_id)

        # Prepare context from Knowledge Base results
        context = "\n".join([result['content']['text'] for result in kb_results])

        # Extract source references from the 'location.s3Location.uri' path
        sources = set()
        for result in kb_results:
            source = result.get('location', {}).get('s3Location', {}).get('uri')
            if source:
                sources.add(source)

        # Generate response using LLM
        full_prompt = f"Context: {context}\n\nUser: {prompt}\n\n"
        response = generate_response(full_prompt, model_id, temperature, top_p)

        # Append sources to response if any found
        if sources:
            source_text = "\n\n---\n**Sources:**\n" + "\n".join(f"- {src}" for src in sources)
            response += source_text
    else:
        response = "I'm unable to answer this, please try again"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
