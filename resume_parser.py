
import re
from PyPDF2 import PdfReader


# Extract text from a PDF resume
def extract_text(pdf_path):
    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as error:
        raise ValueError("Could not read the PDF file.") from error

    return text


# Extract email address
def extract_email(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)

    return match.group(0) if match else "Not found"


# Extract phone number
def extract_phone(text):
    pattern = r"(?<!\w)(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{3,5}\)?[\s.-]?)\d{5,8}(?!\w)"
    match = re.search(pattern, text)

    return match.group(0).strip() if match else "Not found"


# Extract candidate name (best-effort heuristic)
def extract_name(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Skip common resume headings and contact details.
    ignored_headings = {
        "resume",
        "curriculum vitae",
        "cv",
        "profile",
        "contact",
        "contact details",
        "professional summary",
        "summary",
        "objective",
    }

    for line in lines[:10]:
        cleaned = re.sub(r"\s+", " ", line).strip()
        lower_line = cleaned.lower()

        if lower_line in ignored_headings:
            continue

        if "@" in cleaned or re.search(r"\d", cleaned):
            continue

        words = cleaned.split()

        if 2 <= len(words) <= 4 and all(
            re.fullmatch(r"[A-Za-z][A-Za-z'-]*", word) for word in words
        ):
            return cleaned

    return "Not found"


# Identify technical skills
def extract_skills(text):
    known_skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "MySQL",
        "Flask",
        "Django",
        "React",
        "Node.js",
        "PHP",
        "MongoDB",
        "Git",
        "GitHub",
        "AWS",
        "Azure",
        "Machine Learning",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Power BI",
        "Excel",
    ]

    found_skills = []

    for skill in known_skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills if found_skills else ["No known skills detected"]


# Extract education-related lines
def extract_education(text):
    education_keywords = [
        "education",
        "bachelor",
        "master",
        "b.tech",
        "b.e.",
        "b.e ",
        "b.sc",
        "bca",
        "mca",
        "m.tech",
        "degree",
        "diploma",
        "university",
        "college",
        "school",
        "ssc",
        "hsc",
        "12th",
        "10th",
    ]

    education_lines = []

    for line in text.splitlines():
        cleaned = line.strip()

        if not cleaned:
            continue

        if any(
            keyword in cleaned.lower()
            for keyword in education_keywords
        ):
            education_lines.append(cleaned)

    return education_lines if education_lines else ["No education information detected"]


# Main function used by the Flask application
def parse_resume(pdf_path):
    text = extract_text(pdf_path)

    if not text.strip():
        raise ValueError(
            "No readable text was found. The PDF may be scanned or image-based."
        )

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
    }

