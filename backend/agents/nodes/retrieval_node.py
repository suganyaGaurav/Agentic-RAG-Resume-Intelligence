# ==========================================
# Title : retrieval_node.py
#Path : backend/agents/nodes/retrieval_node.py
# Purpose: LangGraph retrieval workflow node.
#
# Responsibilities:
# - perform semantic retrieval
# - retrieve best matching resume chunks
# - store retrieval results into state
# - update workflow status
# - track workflow logs
#
# Why This File Exists:
# This node acts as the:
# "workflow wrapper"
#
# Actual retrieval logic stays inside:
# retrieval_service.py
# ==========================================



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Retrieval Service
# ==========================================

from backend.services.retrieval_service import (
    retrieve_semantic_matches
)



# ==========================================
# Retrieval Node
# ==========================================

def retrieval_node(
    state: ResumeWorkflowState
):


    # --------------------------------------
    # Workflow Start Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Retrieval node started"
    )



    # --------------------------------------
    # Perform Semantic Retrieval
    # --------------------------------------

    retrieval_results = (

        retrieve_semantic_matches(

            state["jd_embeddings"],

            state["resume_vector_store"]

        )

    )



    # --------------------------------------
    # Store Retrieval Results
    # --------------------------------------

    state["retrieved_chunks"] = (
        retrieval_results
    )



    # --------------------------------------
    # Update Workflow Status
    # --------------------------------------

    state["status"] = (
        "retrieval_completed"
    )



    # --------------------------------------
    # Workflow Completion Log
    # --------------------------------------

    state["workflow_logs"].append(
        "Retrieval node completed"
    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state