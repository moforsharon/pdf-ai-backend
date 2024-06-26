import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# Get the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables")

# Initialize the LangChain client with your OpenAI API key
llm = ChatOpenAI(openai_api_key=openai_api_key)
def answer_question(text, question):
    """
    Generates an answer to a question based on the provided document text.

    Args:
        text (str): The text content of the document.
        question (str): The question to be answered.

    Returns:
        str: The generated answer or an error message if processing fails.
    """
    prompt = f"Question: {question}\nDocument: {text}\nAnswer:"
    try:
        # Invoke LangChain with the constructed prompt
        response = llm.invoke(prompt)
        print("Response from LangChain:", response)  # Log the full response
        answer = response.content if hasattr(response, 'content') else "No answer found."
    except Exception as e:
        print("Error:", str(e))  # Log any errors that occur
        answer = f"Failed to process the question: {str(e)}"
    
    return answer
