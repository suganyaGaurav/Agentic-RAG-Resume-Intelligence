# ==========================================
# Title : career_guidance_node.py
# Path : backend/agents/nodes/
#        career_guidance_node.py
#
# Purpose:
# Generate deterministic career guidance
# from analysis results.
#
# Responsibilities:
# - read workflow analysis output
# - read resume intelligence
# - read JD intelligence
# - generate career guidance
# - store guidance in workflow state
# - store career guidance metrics
# - update workflow logs
#
# Why This File Exists:
# Converts resume matching into
# career intelligence.
# ==========================================


# ==========================================
# Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)


# ==========================================
# Career Guidance Service
# ==========================================

from backend.services.career_guidance_service import (
    generate_career_guidance
)


# ==========================================
# Career Guidance Node
# ==========================================

def career_guidance_node(

    state: ResumeWorkflowState

):

    # --------------------------------------
    # Workflow Log
    # --------------------------------------

    state["workflow_logs"].append(

        "Career guidance node started"

    )

    # --------------------------------------
    # Generate Guidance
    # --------------------------------------

    guidance_result = (

        generate_career_guidance(

            state["analysis_result"],

            state["resume_json"],

            state["jd_json"]

        )

    )

    # --------------------------------------
    # Store Guidance
    # --------------------------------------

    state["career_guidance"] = (

        guidance_result

    )

    # --------------------------------------
    # Career Guidance Metrics
    # --------------------------------------

    state["career_guidance_metrics"] = {

        "guidance_generated": True,

        "strength_count":

            len(

                guidance_result.get(
                    "strengths",
                    []
                )

            ),

        "critical_missing_skill_count":

            len(

                guidance_result.get(
                    "critical_missing_skills",
                    []
                )

            ),

        "learning_path_count":

            len(

                guidance_result.get(
                    "learning_path",
                    []
                )

            ),

        "resume_suggestion_count":

            len(

                guidance_result.get(
                    "resume_suggestions",
                    []
                )

            ),

        "overall_score":

            guidance_result.get(
                "overall_score",
                0
            )

    }

    # --------------------------------------
    # Workflow Log
    # --------------------------------------

    state["workflow_logs"].append(

        f"Generated "
        f"{len(guidance_result.get('strengths', []))} "
        f"strengths and "
        f"{len(guidance_result.get('critical_missing_skills', []))} "
        f"critical skill recommendations"

    )

    # --------------------------------------
    # Workflow Status
    # --------------------------------------

    state["status"] = (

        "career_guidance_completed"

    )

    # --------------------------------------
    # Workflow Log
    # --------------------------------------

    state["workflow_logs"].append(

        "Career guidance node completed"

    )

    return state