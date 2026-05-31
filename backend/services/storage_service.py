# ==========================================
# Storage Service
# Purpose:
# Handle secure storage of uploaded files
# into local system directories.
#
# Responsibilities:
# - Create file save paths
# - Save resume PDF
# - Save JD PDF
# - Centralize storage handling
#
# This acts as the file storage layer
# of the system architecture.
# ==========================================


# ==========================================
# Import Required Library
# ==========================================

import os


# ==========================================
# Function:
# Save Uploaded Files
# ==========================================

def save_uploaded_files(resume_file, jd_file):

    # --------------------------------------
    # Create Resume Save Path
    # --------------------------------------

    resume_path = os.path.join(
        "uploads/resumes",
        resume_file.filename
    )


    # --------------------------------------
    # Create JD Save Path
    # --------------------------------------

    jd_path = os.path.join(
        "uploads/job_descriptions",
        jd_file.filename
    )


    # --------------------------------------
    # Save Resume File
    # --------------------------------------

    resume_file.save(resume_path)


    # --------------------------------------
    # Save JD File
    # --------------------------------------

    jd_file.save(jd_path)


    # --------------------------------------
    # Return Saved Paths
    # --------------------------------------

    return {

        "resume_path": resume_path,

        "jd_path": jd_path

    }