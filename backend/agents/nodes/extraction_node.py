# ==========================================
# extraction_node.py
# Purpose:
# AI extraction node for workflow documents.
#
# Responsibilities:
# - mask PII data
# - extract structured intelligence
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
# Intelligence Services
# ==========================================

from backend.services.intelligence_service import (

    mask_pii_data,

    extract_resume_information,

    extract_jd_information

)



# ==========================================
# Extraction Node
# ==========================================

def extraction_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Extraction node started"
    )


    try:


        # ----------------------------------
        # Mask Resume PII Data
        # ----------------------------------

        masked_resume_text = mask_pii_data(

            state["resume_text"]

        )


        # ----------------------------------
        # Mask JD PII Data
        # ----------------------------------

        masked_jd_text = mask_pii_data(

            state["jd_text"]

        )


        # ----------------------------------
        # Store Masked Text
        # ----------------------------------

        state["masked_resume_text"] = (
            masked_resume_text
        )

        state["masked_jd_text"] = (
            masked_jd_text
        )


        # ----------------------------------
        # Extract Structured Resume JSON
        # ----------------------------------

        resume_json = (
            extract_resume_information(

                masked_resume_text

            )
        )


        # ----------------------------------
        # Extract Structured JD JSON
        # ----------------------------------

        jd_json = (
            extract_jd_information(

                masked_jd_text

            )
        )


        # ----------------------------------
        # Store Structured JSON
        # ----------------------------------

        state["resume_json"] = (
            resume_json
        )

        state["jd_json"] = (
            jd_json
        )


        # ----------------------------------
        # Update Workflow Status
        # ----------------------------------

        state["status"] = (
            "extraction_completed"
        )


        # ----------------------------------
        # Workflow Completion Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Extraction node completed"
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
            "Extraction node failed"
        )


        raise Exception(str(error))