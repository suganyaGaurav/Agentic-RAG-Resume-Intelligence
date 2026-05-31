# ==========================================
# Parser Service
# Purpose:
# Extract and normalize text content from
# uploaded PDF documents before entering
# the AI processing pipeline.
#
# Responsibilities:
# - Open PDF files
# - Read PDF pages
# - Extract raw text
# - Clean parser artifacts
# - Normalize spacing
# - Preserve document sections
# - Return structured readable text
#
# Note:
# This acts as the document ingestion layer
# of the AI pipeline.
# ==========================================


# ==========================================
# Import Required Library
# ==========================================

import fitz

import re


# ==========================================
# Function:
# Clean Extracted Text
# Purpose:
# Normalize parser output while preserving
# important resume/JD sections.
# ==========================================

def clean_extracted_text(raw_text):

    # --------------------------------------
    # Remove Multiple Spaces
    # --------------------------------------

    cleaned_text = re.sub(
        r"[ ]+",
        " ",
        raw_text
    )


    # --------------------------------------
    # Normalize Multiple Line Breaks
    # --------------------------------------

    cleaned_text = re.sub(
        r"\n{3,}",
        "\n\n",
        cleaned_text
    )


    # --------------------------------------
    # Remove Leading/Trailing Spaces
    # --------------------------------------

    cleaned_text = cleaned_text.strip()


    # --------------------------------------
    # Return Cleaned Text
    # --------------------------------------

    return cleaned_text


# ==========================================
# Function:
# Extract Text From PDF
# Purpose:
# Extract and clean PDF text content
# ==========================================

def extract_text_from_pdf(pdf_path):

    # --------------------------------------
    # Open PDF Document
    # --------------------------------------

    pdf_document = fitz.open(pdf_path)


    # --------------------------------------
    # Store Extracted Text
    # --------------------------------------

    extracted_text = ""


    # --------------------------------------
    # Read All PDF Pages
    # --------------------------------------

    for page in pdf_document:

        extracted_text += page.get_text()


    # --------------------------------------
    # Close PDF Document
    # --------------------------------------

    pdf_document.close()


    # --------------------------------------
    # Clean Extracted Text
    # --------------------------------------

    cleaned_text = clean_extracted_text(
        extracted_text
    )


    # --------------------------------------
    # Return Cleaned Text
    # --------------------------------------

    return cleaned_text