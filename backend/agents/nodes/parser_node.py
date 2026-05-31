# ==========================================
# parser_node.py
# Purpose:
# PDF parsing node for workflow documents.
#
# Responsibilities:
# - extract text from PDFs
# - update workflow state
# - track workflow logs
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Parser Service
# ==========================================

from backend.services.parser_service import (
    extract_text_from_pdf
)



# ==========================================
# Parser Node
# ==========================================

def parser_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Parser node started"
    )


    try:


        # ----------------------------------
        # Extract Resume PDF Text
        # ----------------------------------

        extracted_resume_text = (
            extract_text_from_pdf(

                state["resume_path"]

            )
        )


        # ----------------------------------
        # Extract JD PDF Text
        # ----------------------------------

        extracted_jd_text = (
            extract_text_from_pdf(

                state["jd_path"]

            )
        )


        # ----------------------------------
        # Store Parsed Text
        # ----------------------------------

        state["resume_text"] = (
            extracted_resume_text
        )

        state["jd_text"] = (
            extracted_jd_text
        )


        # ----------------------------------
        # Update Workflow Status
        # ----------------------------------

        state["status"] = (
            "parsing_completed"
        )


        # ----------------------------------
        # Workflow Completion Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Parser node completed"
        )


        # ----------------------------------
        # Return Updated State
        # ----------------------------------

        return state


    except Exception as error:


        # ----------------------------------
        # Store Workflow Failure
        # ----------------------------------

        state["status"] = (
            "workflow_failed"
        )

        state["error_message"] = (
            str(error)
        )


        # ----------------------------------
        # Workflow Failure Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Parser node failed"
        )


        raise Exception(str(error))