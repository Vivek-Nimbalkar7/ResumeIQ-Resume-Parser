# ResumeIQ — Automated Resume Parser

ResumeIQ is a Python-based web application that extracts important information from PDF resumes. It helps users identify candidate details, technical skills, and education information through a simple web interface.

## Features

* Upload resumes in PDF format.
* Extract candidate names where possible.
* Identify email addresses and phone numbers.
* Detect supported technical skills.
* Extract education-related information.
* Display results on a clean, responsive web page.
* Limit uploaded files to 5 MB.
* Process uploads using temporary files and attempt to delete them after processing.
* Display helpful error messages when a resume cannot be processed.

## Technologies Used

* Python
* Flask
* PyPDF2
* HTML5
* CSS3
* JavaScript
* Regular Expressions
* Git and GitHub

## Project Structure

```text
ResumeIQ-Resume-Parser/
├── app.py
├── resume_parser.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

The Python virtual environment is created locally and is not included in the repository.

## Requirements

* Python 3
* pip
* A modern web browser

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vivek-Nimbalkar7/ResumeIQ-Resume-Parser.git
cd ResumeIQ-Resume-Parser
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv venv
```

### 3. Activate the environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Run the application

```powershell
python app.py
```

### 6. Open the application

Open your browser and visit:

http://127.0.0.1:5000/

## How to Use ResumeIQ

1. Open the ResumeIQ home page.
2. Select a PDF resume.
3. Click the Analyze Resume button.
4. Review the extracted personal information.
5. Check the detected technical skills and education information.
6. Upload another resume if required.

## How It Works

1. Flask receives the uploaded PDF.
2. The application checks the filename extension and upload size.
3. The PDF is temporarily saved.
4. PyPDF2 extracts available text from the PDF.
5. Regular expressions identify email addresses and phone numbers.
6. Simple rules attempt to identify the candidate's name and education.
7. A predefined list of technical skills is checked against the extracted text.
8. Flask displays the results on the results page.
9. The application attempts to delete the temporary PDF.

## Limitations

* Extraction accuracy depends on the resume's layout and text content.
* The candidate's name may not be identified correctly in every resume.
* Education extraction is based on keywords and may include incomplete or unrelated lines.
* Only skills included in the predefined list are detected.
* Scanned or image-based PDFs may not contain extractable text.
* The application does not currently use OCR or a machine-learning model.
* A PDF extension check alone does not guarantee that an uploaded file is safe.

## Security Notes

This project is intended for educational and local demonstration purposes.

* Uploaded files are limited to 5 MB.
* Temporary files are removed after processing when possible.
* Do not upload resumes containing sensitive personal information unless you have permission.
* Flask debug mode should not be enabled in a production deployment.
* A production version would require stronger file validation, additional security controls, and a production-ready web server.

## Future Improvements

* Add OCR support for scanned resumes.
* Improve candidate name and education extraction.
* Expand the technical skills database.
* Add downloadable analysis reports.
* Add automated resume scoring.
* Deploy the application to a hosting platform.

## Author

**Vivek Dipak Nimbalkar**

Third-Year Computer Engineering Student

## License

This project is created for educational and demonstration purposes.
