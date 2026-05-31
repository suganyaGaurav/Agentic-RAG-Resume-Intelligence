# ==========================================
# governance_node.py
# Purpose:
# Governance validation node for uploaded
# workflow files.
#
# Responsibilities:
# - validate uploaded files
# - stop invalid workflow execution
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
# Governance Service
# ==========================================

from backend.services.governance_service import (
    validate_uploaded_files
)



# ==========================================
# Governance Node
# ==========================================

def governance_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Governance node started"
    )



    # --------------------------------------
    # Validate Uploaded Files
    # --------------------------------------

    is_valid, message = validate_uploaded_files(

        state["resume_file"],

        state["jd_file"]

    )



    # --------------------------------------
    # Stop Workflow If Validation Fails
    # --------------------------------------

    if not is_valid:


        # ----------------------------------
        # Update Failure Status
        # ----------------------------------

        state["status"] = (
            "governance_failed"
        )



        # ----------------------------------
        # Store Error Message
        # ----------------------------------

        state["error_message"] = (
            message
        )



        # ----------------------------------
        # Workflow Failure Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Governance validation failed"
        )



        # ----------------------------------
        # Stop Workflow Execution
        # ----------------------------------

        raise Exception(message)



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "governance_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Governance node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state