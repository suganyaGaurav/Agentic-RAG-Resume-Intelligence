# ==========================================
# Title : extraction_node.py
# Path : backend/agents/nodes/extraction_node.py
# Purpose: AI extraction node for workflow documents.
#
# Responsibilities:
# - mask PII data
# - extract structured intelligence
# - update workflow state
# - track workflow logs
# - collect extraction telemetry
# ==========================================

# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)

# ==========================================
# Extraction Services
# ==========================================

from backend.services.extraction_service import (

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

    # --------------------------------------
    # Extraction Telemetry Start
    # --------------------------------------

    state["extraction_metrics"] = {

        "resume_text_length": len(
            state["resume_text"]
        ),

        "jd_text_length": len(
            state["jd_text"]
        ),

        "resume_skill_count": 0,

        "jd_skill_count": 0,

        "pii_masking_completed": False,

        "extraction_success": False,

        "extraction_message": "",

        "error": None,

        "error_type": None

    }

    try:

        # ----------------------------------
        # Mask Resume PII Data
        # ----------------------------------

        masked_resume_text = (
            mask_pii_data(
                state["resume_text"]
            )
        )

        # ----------------------------------
        # Mask JD PII Data
        # ----------------------------------

        masked_jd_text = (
            mask_pii_data(
                state["jd_text"]
            )
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
        # Update PII Metrics
        # ----------------------------------

        state["extraction_metrics"][
            "pii_masking_completed"
        ] = True

        # ----------------------------------
        # Extract Resume Intelligence
        # ----------------------------------

        resume_json = (
            extract_resume_information(
                masked_resume_text
            )
        )

        # ----------------------------------
        # Extract JD Intelligence
        # ----------------------------------

        jd_json = (
            extract_jd_information(
                masked_jd_text
            )
        )

        # ----------------------------------
        # Store Structured Output
        # ----------------------------------

        state["resume_json"] = (
            resume_json
        )

        state["jd_json"] = (
            jd_json
        )

        # ----------------------------------
        # Resume Skill Count
        # ----------------------------------

        resume_skill_count = 0

        for skill_list in (

            resume_json
                .get(
                    "skills",
                    {}
                )
                .values()

        ):

            resume_skill_count += len(
                skill_list
            )

        # ----------------------------------
        # JD Skill Count
        # ----------------------------------

        jd_skill_count = 0

        for skill_list in (

            jd_json
                .get(
                    "skills",
                    {}
                )
                .values()

        ):

            jd_skill_count += len(
                skill_list
            )

        # ----------------------------------
        # Store Skill Metrics
        # ----------------------------------

        state["extraction_metrics"][
            "resume_skill_count"
        ] = resume_skill_count

        state["extraction_metrics"][
            "jd_skill_count"
        ] = jd_skill_count

        # ----------------------------------
        # Extraction Success Metrics
        # ----------------------------------

        state["extraction_metrics"][
            "extraction_success"
        ] = True

        state["extraction_metrics"][
            "extraction_message"
        ] = (
            "Extraction completed successfully"
        )

        state["extraction_metrics"][
            "error_type"
        ] = None

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
        # Workflow Failure Status
        # ----------------------------------

        state["status"] = (
            "workflow_failed"
        )

        state["error_message"] = (
            str(error)
        )

        # ----------------------------------
        # Extraction Failure Metrics
        # ----------------------------------

        state["extraction_metrics"][
            "extraction_success"
        ] = False

        state["extraction_metrics"][
            "extraction_message"
        ] = (
            "Extraction failed"
        )

        state["extraction_metrics"][
            "error"
        ] = str(error)

        state["extraction_metrics"][
            "error_type"
        ] = (
            "extraction_failure"
        )

        # ----------------------------------
        # Workflow Failure Log
        # ----------------------------------

        state["workflow_logs"].append(

            f"Extraction node failed: {str(error)}"

        )

        # ----------------------------------
        # Preserve Original Traceback
        # ----------------------------------

        raise