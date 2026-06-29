# ======================================
# Storage Metrics
# Purpose:
# Stores file storage execution metrics
# for observability dashboards and audits.
#
# Example:
# - resume_uploaded
# - jd_uploaded
# - resume_filename
# - jd_filename
# - resume_path
# - jd_path
# - storage_success
# - storage_message
# - error
# - error_type
# ======================================

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

    # --------------------------------------
    # Storage Telemetry Start
    # --------------------------------------

    state["storage_metrics"] = {

        "resume_uploaded": bool(
            state["resume_file"]
        ),

        "jd_uploaded": bool(
            state["jd_file"]
        ),

        "resume_filename": "",

        "jd_filename": "",

        "resume_path": "",

        "jd_path": "",

        "storage_success": False,

        "storage_message": "",

        "error": None,

        "error_type": None

    }

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
        # Storage Success Metrics
        # ----------------------------------

        state["storage_metrics"][
            "resume_filename"
        ] = state["resume_file"].filename

        state["storage_metrics"][
            "jd_filename"
        ] = state["jd_file"].filename

        state["storage_metrics"][
            "resume_path"
        ] = state["resume_path"]

        state["storage_metrics"][
            "jd_path"
        ] = state["jd_path"]

        state["storage_metrics"][
            "storage_success"
        ] = True

        state["storage_metrics"][
            "storage_message"
        ] = "Files stored successfully"

        state["storage_metrics"][
            "error_type"
        ] = None

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
        # Storage Failure Metrics
        # ----------------------------------

        state["storage_metrics"][
            "storage_success"
        ] = False

        state["storage_metrics"][
            "storage_message"
        ] = "File storage failed"

        state["storage_metrics"][
            "error"
        ] = str(error)

        state["storage_metrics"][
            "error_type"
        ] = "storage_failure"

        # ----------------------------------
        # Workflow Failure Log
        # ----------------------------------

        state["workflow_logs"].append(
            f"Storage node failed: {str(error)}"
        )

        # ----------------------------------
        # Re-raise Exception
        # ----------------------------------

        raise