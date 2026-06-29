# ==========================================
# Title : parser_node.py
# Path : backend/agents/nodes/parser_node.py
# Purpose: PDF parsing node for workflow documents.
#
# Responsibilities:
# - extract text from PDFs
# - update workflow state
# - track workflow logs
# - collect parser telemetry
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

    # --------------------------------------
    # Parser Telemetry Start
    # --------------------------------------

    state["parser_metrics"] = {

        "resume_path": state["resume_path"],

        "jd_path": state["jd_path"],

        "resume_characters": 0,

        "jd_characters": 0,

        "parser_success": False,

        "parser_message": "",

        "error": None,

        "error_type": None

    }

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
        # Parser Success Metrics
        # ----------------------------------

        state["parser_metrics"][
            "resume_characters"
        ] = len(extracted_resume_text)

        state["parser_metrics"][
            "jd_characters"
        ] = len(extracted_jd_text)

        state["parser_metrics"][
            "parser_success"
        ] = True

        state["parser_metrics"][
            "parser_message"
        ] = (
            "PDF parsing completed successfully"
        )

        state["parser_metrics"][
            "error_type"
        ] = None

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

        # ----------------------------------
        # Handle Known Parser Errors
        # ----------------------------------

        if str(error) == (
            "NO_EXTRACTABLE_TEXT_FOUND"
        ):

            state["error_message"] = (

                "No readable text could be "
                "extracted from the uploaded PDF. "
                "The file may be empty, image-only, "
                "or contain unsupported content."

            )

            state["parser_metrics"][
                "error_type"
            ] = "no_extractable_text"

        else:

            state["error_message"] = (
                str(error)
            )

            state["parser_metrics"][
                "error_type"
            ] = "parser_failure"

        # ----------------------------------
        # Parser Failure Metrics
        # ----------------------------------

        state["parser_metrics"][
            "parser_success"
        ] = False

        state["parser_metrics"][
            "parser_message"
        ] = "PDF parsing failed"

        state["parser_metrics"][
            "error"
        ] = str(error)

        # ----------------------------------
        # Workflow Failure Log
        # ----------------------------------

        state["workflow_logs"].append(
            f"Parser node failed: {str(error)}"
        )

        # ----------------------------------
        # Preserve Original Traceback
        # ----------------------------------

        raise