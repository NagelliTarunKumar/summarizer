import fitz  # PyMuPDF
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained summarization model and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text if text.strip() else "No readable text found in the PDF."
    except Exception as e:
        return f"Error extracting text: {str(e)}"

# Function to summarize text
def summarize_text(text, max_length=150):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(**inputs, max_length=max_length, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Home route (landing page)
@app.route('/')
def home():
    return "healthy"


# API Endpoint to summarize text from a PDF
@app.route('/summarize', methods=['POST'])
def summarize_pdf():

    if 'pdf_file' not in request.files:
        return jsonify({"error": "No PDF file uploaded."}), 400

    file = request.files['pdf_file']
    pdf_path = "/tmp/temp.pdf"
    file.save(pdf_path)

    extracted_text = extract_text_from_pdf(pdf_path)

    if extracted_text.startswith("Error") or extracted_text == "No readable text found in the PDF.":
        return jsonify({"error": extracted_text}), 400

    existing_summary = request.form.get("existing_summary")
    if existing_summary is None:
        existing_summary = ""

    summary = summarize_text(existing_summary+extracted_text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
