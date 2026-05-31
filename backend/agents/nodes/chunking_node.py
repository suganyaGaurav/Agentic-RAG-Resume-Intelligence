# ==========================================
# chunking_node.py
# Purpose:
# LangGraph chunking workflow node.
#
# Responsibilities:
# - convert structured extraction JSON
#   into semantic competency chunks
# - store chunks into workflow state
# - update workflow status
# - track workflow logs
#
# Why This File Exists:
# This node acts as the:
# "workflow wrapper"
#
# Actual chunking logic stays inside:
# chunking_service.py
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Chunking Service
# ==========================================

from backend.services.chunking_service import (
    create_semantic_chunks
)



# ==========================================
# Chunking Node
# ==========================================

def chunking_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Chunking node started"
    )



    # --------------------------------------
    # Create Resume Chunks
    # --------------------------------------

    resume_chunks = create_semantic_chunks(

        state["resume_json"]

    )



    # --------------------------------------
    # Create JD Chunks
    # --------------------------------------

    jd_chunks = create_semantic_chunks(

        state["jd_json"]

    )



    # --------------------------------------
    # Store Resume Chunks
    # --------------------------------------

    state["resume_chunks"] = (
        resume_chunks
    )



    # --------------------------------------
    # Store JD Chunks
    # --------------------------------------

    state["jd_chunks"] = (
        jd_chunks
    )



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "chunking_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Chunking node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state