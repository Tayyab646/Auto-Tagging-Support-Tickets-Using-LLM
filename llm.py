# 1. INSTALLATION
!pip install -q -U langchain-groq langchain-core pandas==2.2.2 gradio

import os
import pandas as pd
import gradio as gr
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# 2. CONFIGURATION
os.environ["GROQ_API_KEY"] = "your-api-key here" # <--- Paste your key here
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

# 3. TAXONOMY
possible_tags = ["Billing & Payments", "Technical Issue", "Account Access", "Feature Request", "Cancellation Request", "Refund", "Product Inquiry", "Network Problem", "Software Bug"]

# 4. VARIABLE-SAFE PROMPT
# We use double braces {{ }} for the JSON example so LangChain treats them as text, not variables.
system_message = """You are a support ticket classification system.
Tags must be chosen from this list: {tags_list}.
Return exactly 3 tags in order of probability.

Output Format: JSON only, exactly like this: {{ "tags": ["Tag1", "Tag2", "Tag3"] }}"""

few_shot_examples = """
Examples of how to tag:
Ticket: "I can't log in to my account, password reset failed." -> Tags: ["Account Access", "Technical Issue", "Product Inquiry"]
Ticket: "Double charge on my visa card." -> Tags: ["Billing & Payments", "Refund", "Product Inquiry"]
"""

def tag_ticket(ticket_text, mode="Few-Shot"):
    # Combine the system instructions
    full_instructions = system_message
    if mode == "Few-Shot":
        full_instructions += few_shot_examples

    # Define the template with clear variables
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", full_instructions),
        ("human", "{input_text}")
    ])

    # Build the chain
    chain = prompt_template | llm | JsonOutputParser()

    try:
        # We pass both the list and the ticket text here
        result = chain.invoke({
            "tags_list": possible_tags,
            "input_text": ticket_text
        })
        return result["tags"]
    except Exception as e:
        # This will show you exactly if it's an API error or a Parsing error
        return [f"Error: {str(e)[:100]}", "N/A", "N/A"]

# 5. GRADIO INTERFACE
def process_ui(text, mode):
    if not text.strip():
        return "Please enter ticket text."
    tags = tag_ticket(text, mode)
    return " | ".join(tags)

demo = gr.Interface(
    fn=process_ui,
    inputs=[
        gr.Textbox(label="Customer Support Ticket", placeholder="Type the customer issue here..."),
        gr.Radio(["Zero-Shot", "Few-Shot"], label="Classification Mode", value="Few-Shot")
    ],
    outputs=gr.Textbox(label="Top 3 Predicted Tags"),
    title="Auto Tagging Support Tickets",
    description="This system uses Prompt Engineering to automatically categorize support requests."
)

if __name__ == "__main__":
    demo.launch(share=True)
