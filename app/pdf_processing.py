import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content from the PDF.
    """
    doc = fitz.open(file_path)
    text = ""
    
    # Iterate through each page in the PDF and extract text
    for page in doc:
        text += page.get_text()
    
    return text
