# Financial Report Extractor

The Financial Report Extractor is an innovative tool designed to automate the extraction of key financial data from PDF reports. It uses Google Generative AI (Gemini) with a Python-Flask backend to extract the company name, quarter information, and critical financial metrics (such as RevenueSales, Operating Profit, and Net Profit) and display them in a strictly structured HTML format.

The output format is enforced via a detailed prompt to ensure 100% accuracy.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Prompt & Formatting Rules](#prompt--formatting-rules)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

## Overview

Manually extracting financial data from PDF reports is tedious and error-prone. The Financial Report Extractor automates this process by leveraging AI to extract structured data directly from PDFs. The tool outputs

- Company Name Displayed as an `h2` heading.
- Quarter Information Shown in a `p` element immediately below the company name.
- Financial Data Presented in a clean HTML table with rows for each financial parameter (e.g., RevenueSales, Operating Profit, Net Profit) and columns for Consolidated and Standalone values (omitting any column that lacks data).

## Features

- Automated Extraction Extract key financial data using Google Generative AI.
- Strictly Structured Output Enforces a defined HTML structure using a detailed prompt.
- Conditional Column Handling Omits empty columns (ConsolidatedStandalone) for clarity.
- User-Friendly Web Interface Built with Flask, allowing users to select a PDF and view results instantly.
- Extensible Designed for accuracy with room for further enhancements.

## Technology Stack

- Backend Python, Flask
- AI Integration Google Generative AI (Gemini)
- HTML Parsing BeautifulSoup
- Frontend HTML, CSS, Bootstrap

## Installation

1. Clone the Repository

   ```bash
   git clone https:\\github.com\prit-zalavadiya-78\financial-report-extractor.git
   cd financial-report-extractor
   ```

2. Install Dependencies
   ```bash
   pip install flask, beautifulsoup4, google-generativeai
   ```

3. Configure API Key and PDF Folder

   In `app.py`, update the API key
   ```python
   genai.configure(api_key=YOUR_API_KEY)
   ```
   And set `PDF_FOLDER` to the directory containing your PDF reports
   ```python
   PDF_FOLDER = pathtoyourpdffolder
   ```

## Usage

1. Run the Application

   ```bash
   python app.py
   ```

2. Open the Web Interface

   Navigate to [http:\\127.0.0.15000](http:\\127.0.0.15000) in your browser.

3. Process a PDF

   - Select a PDF from the dropdown list.
   - Click Extract Data.
   - The extracted company name, quarter information, and financial table (with only available columns) will be displayed.

## Prompt & Formatting Rules

To ensure 100% accurate output, the following prompt is used when generating the content

```python
""" Extract the company's name and only current quarter's financial results (RevenueSales, Operating Profit(Profit before tax), Net Profit, Time period of extracted data, Consolidated and Standalone, Unit) 
from the report and format them as a clean HTML output. 
Ensure the company's name is displayed as a heading, followed by a properly formatted table with financial data. 
Do NOT add any extra text, explanations, or irrelevant details. """
```

This prompt is passed to the Gemini AI model along with the PDF content to produce the structured output.

## Project Structure

```
financial-report-extractor
└── Code
    ├── app.py                # Main Flask application
    └── templates
        └── index.html        # Frontend HTML file
└── README.md                 # Project documentation
```

## Future Improvements

- Enhanced Prompt Tuning Further refine the prompt for even higher accuracy.
- Robust Error Handling Improve support for varied PDF formats and edge cases.
- Unit Testing Add tests to ensure consistent output across different reports.
- UIUX Enhancements Expand interactive features (e.g., live search, filtering, dynamic charts).
- Cloud Deployment Prepare the application for scalable cloud deployment.

Developed for the MINeD 2025 on 2nd Feb, 2025.
