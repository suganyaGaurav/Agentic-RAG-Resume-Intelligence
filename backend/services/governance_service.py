# ==========================================
# governance_service.py
# Purpose:
# Validate uploaded files before they enter
# the AI workflow pipeline.
#
# Responsibilities:
# - Check empty uploads
# - Enforce PDF-only uploads
# - Validate resume-like content
# - Validate JD-like content
# - Reject invalid document types
#
# Why This File Is Important:
# This acts as the:
# "Governance and Input Validation Layer"
#
# The goal is to stop:
# - invalid uploads
# - wrong document types
# - noisy workflow execution
#
# Example:
# JD uploaded as Resume
# → workflow should stop
#
# Resume uploaded as JD
# → workflow should stop
# ==========================================



# ==========================================
# Import Required Libraries
# ==========================================

import re

import fitz



# ==========================================
# Allowed File Extensions
# ==========================================

ALLOWED_EXTENSIONS = {"pdf"}



# ==========================================
# Function:
# Validate Allowed File Type
# ==========================================

def allowed_file(filename):

    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS



# ==========================================
# Function:
# Extract Quick PDF Text
#
# Purpose:
# Extract limited text content for
# governance validation checks
# ==========================================

def extract_quick_text(pdf_file):

    extracted_text = ""


    # --------------------------------------
    # Open PDF From Uploaded File
    # --------------------------------------

    pdf_document = fitz.open(

        stream=pdf_file.read(),

        filetype="pdf"

    )


    # --------------------------------------
    # Read First Few Pages
    # --------------------------------------

    for page in pdf_document[:3]:

        extracted_text += page.get_text()


    # --------------------------------------
    # Reset File Pointer
    # --------------------------------------

    pdf_file.seek(0)


    return extracted_text.lower()



# ==========================================
# Function:
# Validate Resume Content
# ==========================================

def is_resume_document(text):


    # --------------------------------------
    # Resume Indicators
    # --------------------------------------

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    phone_pattern = r"\+?\d[\d\s\-]{8,}"


    resume_keywords = [

        "experience",

        "education",

        "skills",

        "projects",

        "certifications",

        "linkedin",

        "github"

    ]


    # --------------------------------------
    # Check Email / Phone
    # --------------------------------------

    has_email = re.search(

        email_pattern,

        text

    )


    has_phone = re.search(

        phone_pattern,

        text

    )


    # --------------------------------------
    # Check Resume Keywords
    # --------------------------------------

    keyword_matches = sum(

        keyword in text

        for keyword in resume_keywords

    )


    # --------------------------------------
    # Resume Validation Logic
    # --------------------------------------

    if (has_email or has_phone) and keyword_matches >= 2:

        return True


    return False



# ==========================================
# Function:
# Validate JD Content
# ==========================================

def is_jd_document(text):


    # --------------------------------------
    # JD Keywords
    # --------------------------------------

    jd_keywords = [

        "responsibilities",

        "requirements",

        "qualifications",

        "job description",

        "preferred skills",

        "mandatory skills",

        "experience required",

        "role",

        "candidate",

        "hiring"

    ]


    # --------------------------------------
    # Count JD Keyword Matches
    # --------------------------------------

    keyword_matches = sum(

        keyword in text

        for keyword in jd_keywords

    )


    # --------------------------------------
    # JD Validation Logic
    # --------------------------------------

    if keyword_matches >= 2:

        return True


    return False



# ==========================================
# Function:
# Validate Uploaded Files
# ==========================================

def validate_uploaded_files(

    resume_file,

    jd_file

):


    # --------------------------------------
    # Check Empty Uploads
    # --------------------------------------

    if (

        resume_file.filename == ""

        or

        jd_file.filename == ""

    ):

        return False, (

            "Both PDF files are required"

        )



    # --------------------------------------
    # Validate Resume File Format
    # --------------------------------------

    if not allowed_file(

        resume_file.filename

    ):

        return False, (

            "Resume must be a PDF file"

        )



    # --------------------------------------
    # Validate JD File Format
    # --------------------------------------

    if not allowed_file(

        jd_file.filename

    ):

        return False, (

            "Job Description must be a PDF file"

        )



    # --------------------------------------
    # Extract Quick Resume Text
    # --------------------------------------

    resume_text = extract_quick_text(

        resume_file

    )



    # --------------------------------------
    # Extract Quick JD Text
    # --------------------------------------

    jd_text = extract_quick_text(

        jd_file

    )



    # --------------------------------------
    # Validate Resume Content
    # --------------------------------------

    if not is_resume_document(

        resume_text

    ):

        return False, (

            "Uploaded resume does not appear to be a valid resume document"

        )



    # --------------------------------------
    # Validate JD Content
    # --------------------------------------

    if not is_jd_document(

        jd_text

    ):

        return False, (

            "Uploaded JD does not appear to contain job requirements"

        )



    # --------------------------------------
    # Prevent Same Document Upload
    # --------------------------------------

    if resume_text[:1000] == jd_text[:1000]:

        return False, (

            "Resume and JD appear to be the same document"

        )



    # --------------------------------------
    # Validation Success
    # --------------------------------------

    return True, "Validation Successful"