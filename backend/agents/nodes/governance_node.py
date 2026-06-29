# ==========================================

# Title : governance_node.py
# Path : backend/agents/nodes/governance_node.py

# Purpose:
# Governance validation node for uploaded
# workflow files.

# Responsibilities:
# - validate uploaded files
# - stop invalid workflow execution
# - update workflow state
# - update governance telemetry
# - track workflow logs

# Notes:
# This node executes before any AI
# processing begins.

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

    print(
        "\n===== GOVERNANCE NODE EXECUTED =====\n"
    )

    
    print(
        "\n===== GOVERNANCE NODE EXECUTED =====\n"
    )

    print(
        "Resume:",
        state.get("resume_file")
    )

    print(
        "JD:",
        state.get("jd_file")
    )

    print(
        "CALLING validate_uploaded_files()"
    )
    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Governance node started"
    )

    # --------------------------------------
    # Governance Telemetry Start
    # --------------------------------------

    state["governance_metrics"] = {

        "resume_uploaded": bool(
            state["resume_file"]
        ),

        "jd_uploaded": bool(
            state["jd_file"]
        ),

        "governance_passed": False,

        "validation_message": "",

        "error_type": None

    }

    try:

        # ----------------------------------
        # Validate Uploaded Files
        # ----------------------------------

        print(
            "Resume:",
            state["resume_file"]
        )
        
        print(
            "JD:",
            state["jd_file"]
        )
        
        is_valid, message = validate_uploaded_files(

            state["resume_file"],

            state["jd_file"]

        )

        # ----------------------------------
        # Validation Failure
        # ----------------------------------

        if not is_valid:

            state["status"] = (
                "governance_failed"
            )

            state["error_message"] = (
                message
            )

            state["governance_metrics"][
                "governance_passed"
            ] = False

            state["governance_metrics"][
                "validation_message"
            ] = message

            state["governance_metrics"][
                "error_type"
            ] = "validation_failure"

            state["workflow_logs"].append(
                f"Governance validation failed: {message}"
            )

            raise Exception(message)

        # ----------------------------------
        # Governance Success Metrics
        # ----------------------------------

        state["governance_metrics"][
            "governance_passed"
        ] = True

        state["governance_metrics"][
            "validation_message"
        ] = "Files validated successfully"

        state["governance_metrics"][
            "error_type"
        ] = None

        # ----------------------------------
        # Update Workflow Status
        # ----------------------------------

        state["status"] = (
            "governance_completed"
        )

        # ----------------------------------
        # Workflow Completion Log
        # ----------------------------------

        state["workflow_logs"].append(
            "Governance node completed"
        )

        return state

    except Exception as error:

        # ----------------------------------
        # Avoid Duplicate Logging For
        # Validation Failures
        # ----------------------------------

        if state["governance_metrics"].get(
            "error_type"
        ) == "validation_failure":

            raise

        # ----------------------------------
        # Unexpected System Failure
        # ----------------------------------

        state["status"] = (
            "governance_failed"
        )

        state["error_message"] = (
            str(error)
        )

        state["governance_metrics"][
            "governance_passed"
        ] = False

        state["governance_metrics"][
            "validation_message"
        ] = str(error)

        state["governance_metrics"][
            "error_type"
        ] = "system_failure"

        state["workflow_logs"].append(
            f"Governance node failed: {str(error)}"
        )

        raise