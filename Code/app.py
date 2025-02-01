import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup


# Configure Gemini AI
genai.configure(api_key="YOUR_API_KEY") # Gemini AI API key
model = genai.GenerativeModel("gemini-2.0-flash-exp")

app = Flask(__name__)
PDF_FOLDER = "path/to/your/pdf/folder/"  # Folder where PDFs are stored

# Route to display the webpage
@app.route('/')
def index():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]
    return render_template('index.html', pdf_files=pdf_files)
    
@app.route('/process', methods=['POST'])
def process():
    pdf_name = request.form['pdf_file']
    pdf_path = os.path.join(PDF_FOLDER, pdf_name)

    # Upload the PDF
    sample_pdf = genai.upload_file(pdf_path)

    # Modify prompt to return structured data
    response = model.generate_content([
        "Extract the company's name and only current **quarter**'s financial results (Revenue/Sales, Operating Profit(Profit before tax), Net Profit, Time period of extracted data, Consolidated and Standalone, Unit) "
        "from the report and format them as a clean HTML output. "
        "Ensure the company's name is displayed as a heading, followed by a properly formatted <table> with financial data. "
        "Do NOT add any extra text, explanations, or irrelevant details.",
        sample_pdf
    ])
    
    # Parse the HTML output
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the table and company name
    table = soup.find("table")  # Extract only the table
    heading = soup.find(["h1", "h2", "h3", "p"])  # Try to find a company name heading

    # Construct clean output
    clean_html = ""
    if heading:
        clean_html += f"<h2>{heading.text}</h2>"  # Keep only the company name as a heading
    if table:
        clean_html += str(table)  # Keep only the financial table
    if not clean_html:
        clean_html = "<p>No valid data found.</p>"

    return jsonify({"result": clean_html})  # Return cleaned HTML



if __name__ == '__main__':
    app.run(debug=True)
