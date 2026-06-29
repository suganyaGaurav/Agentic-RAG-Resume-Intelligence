# ==========================================
# Title : embedding_node.py
# Path : backend/agents/nodes/embedding_node.py
# Purpose: LangGraph embedding workflow node.
#
# Responsibilities:
# - generate semantic embeddings
# - store embeddings into workflow state
# - update workflow status
# - track workflow logs
#
# Why This File Exists:
# This node acts as the:
# "workflow wrapper"
#
# Actual embedding logic stays inside:
# embedding_service.py
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Embedding Service
# ==========================================

from backend.services.embedding_service import (
    generate_chunk_embeddings
)



# ==========================================
# Embedding Node
# ==========================================

def embedding_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Embedding node started"
    )



    # --------------------------------------
    # Generate Resume Embeddings
    # --------------------------------------

    resume_embeddings = generate_chunk_embeddings(

        state["resume_chunks"]

    )



    # --------------------------------------
    # Generate JD Embeddings
    # --------------------------------------

    jd_embeddings = generate_chunk_embeddings(

        state["jd_chunks"]

    )



    # --------------------------------------
    # Store Resume Embeddings
    # --------------------------------------

    state["resume_embeddings"] = (
        resume_embeddings
    )



    # --------------------------------------
    # Store JD Embeddings
    # --------------------------------------

    state["jd_embeddings"] = (
        jd_embeddings
    )



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "embedding_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Embedding node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state