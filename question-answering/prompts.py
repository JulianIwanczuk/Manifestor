from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """You are a personal growth assistant. Your task is to help the user with their path of spiritual and personal transformation, using the personal information about the user provided in the document to help them based on their current situation.

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
