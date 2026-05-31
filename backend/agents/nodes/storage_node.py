# ==========================================
# storage_node.py
# Purpose:
# File storage node for uploaded workflow
# documents.
#
# Responsibilities:
# - save uploaded files
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
# Storage Service
# ==========================================

from backend.services.storage_service import (
    save_uploaded_files
)



# ==========================================
# Storage Node
# ==========================================

def storage_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Storage node started"
    )


    try:


        # ----------------------------------
        # Save Uploaded Files
        # ----------------------------------

        saved_files = save_uploaded_files(

            state["resume_file"],

            state["jd_file"]

        )


        # ----------------------------------
        # Store Resume Save Path
        # ----------------------------------

        state["resume_path"] = (
            saved_files["resume_path"]
        )


        # ----------------------------------
        # Store JD Save Path
        # ----------------------------------

        state["jd_path"] = (
            saved_files["jd_path"]
        )


        # ----------------------------------
        # Update Workflow Status
        # ----------------------------------

        state["status"] = (
            "storage_completed"
        )


        # ----------------------------------
        # Workflow Completion Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Storage node completed"
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
            "Storage node failed"
        )


        raise Exception(str(error))