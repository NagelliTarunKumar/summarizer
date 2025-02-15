import requests

# Define the API endpoint
url = "http://localhost:8080/summarize_pdf"

# Specify the PDF file to upload (replace with your actual file path)
pdf_file_path = "/Users/tarunkumarnagelli/Downloads/Tarun_Resume_Sep_6.pdf"  # Ensure this file exists in the same directory

# Open the PDF file in binary mode
with open(pdf_file_path, "rb") as file:
    files = {"pdf_file": file}

    # Make a POST request to the API
    response = requests.post(url, files=files)

# Print the response

print("Response JSON:", response.json())
