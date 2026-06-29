# ==========================================
# Title : vector_store_node.py
# Path : backend/agents/nodes/vector_store_node.py
# Purpose: LangGraph vector store workflow node.
#
# Responsibilities:
# - create FAISS vector stores
# - store vector databases into state
# - update workflow status
# - track workflow logs
#
# Why This File Exists:
# This node acts as the:
# "workflow wrapper"
#
# Actual FAISS logic stays inside:
# vector_store_service.py
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Vector Store Service
# ==========================================

from backend.services.vector_store_service import (
    build_faiss_index
)



# ==========================================
# Vector Store Node
# ==========================================

def vector_store_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Vector store node started"
    )



    # --------------------------------------
    # Build Resume FAISS Index
    # --------------------------------------

    resume_vector_store = build_faiss_index(

        state["resume_embeddings"]

    )



    # --------------------------------------
    # Build JD FAISS Index
    # --------------------------------------

    jd_vector_store = build_faiss_index(

        state["jd_embeddings"]

    )



    # --------------------------------------
    # Store Resume Vector Store
    # --------------------------------------

    state["resume_vector_store"] = (
        resume_vector_store
    )



    # --------------------------------------
    # Store JD Vector Store
    # --------------------------------------

    state["jd_vector_store"] = (
        jd_vector_store
    )



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "vector_store_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Vector store node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state