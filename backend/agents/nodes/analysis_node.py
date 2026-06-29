# ==========================================
# Title : analysis_node.py
# Path : backend/agents/nodes/analysis_node.py
# Purpose: LangGraph analysis workflow node.
#
# Responsibilities:
# - analyze retrieval results
# - generate match intelligence
# - determine support eligibility
# - store analysis results into state
# - update workflow status
# - track workflow logs
#
# Why This File Exists:
# This node acts as the:
# "workflow wrapper"
#
# Actual analysis logic stays inside:
# analysis_service.py
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Analysis Service
# ==========================================

from backend.services.analysis_service import (
    analyze_retrieval_results
)



# ==========================================
# Analysis Node
# ==========================================

def analysis_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Analysis node started"
    )



    # --------------------------------------
    # Analyze Retrieval Results
    # --------------------------------------

    analysis_result = (

        analyze_retrieval_results(

            state["retrieved_chunks"]

        )

    )



    # --------------------------------------
    # Store Analysis Results
    # --------------------------------------

    state["analysis_result"] = (
        analysis_result
    )



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "analysis_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Analysis node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state