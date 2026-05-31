# ==========================================
# evaluation_node.py
# Purpose:
# Execute deterministic evaluation logic
# after semantic retrieval and analysis.
#
# Responsibilities:
# - read retrieval results
# - read analysis outputs
# - invoke evaluation service
# - store evaluation metrics
# - update workflow logs
#
# Why This File Exists:
# Evaluation should remain:
# - modular
# - observable
# - independently testable
#
# This node validates:
# - retrieval quality
# - scoring realism
# - semantic match consistency
# ==========================================



# ==========================================
# Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Evaluation Service
# ==========================================

from backend.services.evaluation_service import (
    evaluate_retrieval_quality
)



# ==========================================
# Function:
# Evaluation Node
# ==========================================

def evaluation_node(

    state: ResumeWorkflowState

):


    # --------------------------------------
    # Read Analysis Result
    # --------------------------------------

    analysis_result = (
        state["analysis_result"]
    )



    # --------------------------------------
    # Read Retrieval Results
    # --------------------------------------

    retrieval_results = (
        state["retrieved_chunks"]
    )



    # --------------------------------------
    # Execute Evaluation Service
    # --------------------------------------

    evaluation_metrics = (
        evaluate_retrieval_quality(

            analysis_result,

            retrieval_results

        )
    )



    # --------------------------------------
    # Store Evaluation Metrics
    # --------------------------------------

    state["evaluation_metrics"] = (
        evaluation_metrics
    )



    # --------------------------------------
    # Workflow Logging
    # --------------------------------------

    state["workflow_logs"].append(

        "Evaluation node completed"

    )



    # --------------------------------------
    # Return Updated State
    # --------------------------------------

    return state