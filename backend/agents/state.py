# ==========================================
# state.py
# Purpose:
# Shared workflow memory used across all
# LangGraph nodes.
#
# This state object stores:
# - uploaded files
# - parsed text
# - masked text
# - structured extraction output
# - workflow logs
# - workflow errors
# - semantic retrieval outputs
# - analysis outputs
# - evaluation metrics
#
# Each workflow node:
# - reads data from state
# - updates state
# - passes state forward
#
# Example Flow:
#
# Flask
# → Governance Node
# → Storage Node
# → Parser Node
# → Extraction Node
# → Chunking Node
# → Embedding Node
# → Retrieval Node
# → Analysis Node
# → Evaluation Node
# ==========================================



# ==========================================
# Imports
# ==========================================

from typing import TypedDict

from typing import Dict

from typing import List

from typing import Any



# ==========================================
# Workflow State
# ==========================================

class ResumeWorkflowState(TypedDict):


    # ======================================
    # Uploaded Files
    # ======================================

    resume_file: Any

    jd_file: Any



    # ======================================
    # Saved File Paths
    # ======================================

    resume_path: str

    jd_path: str



    # ======================================
    # Parsed Text
    # ======================================

    resume_text: str

    jd_text: str



    # ======================================
    # Masked Governance-Safe Text
    # ======================================

    masked_resume_text: str

    masked_jd_text: str



    # ======================================
    # Structured Extraction Output
    # ======================================

    resume_json: Dict[str, Any]

    jd_json: Dict[str, Any]



    # ======================================
    # Workflow Observability
    # ======================================

    workflow_logs: List[str]

    error_message: str



    # ======================================
    # Chunking Outputs
    # ======================================

    resume_chunks: List[Dict[str, Any]]

    jd_chunks: List[Dict[str, Any]]



    # ======================================
    # Embedding Outputs
    # ======================================

    resume_embeddings: List[Dict[str, Any]]

    jd_embeddings: List[Dict[str, Any]]



    # ======================================
    # Vector Store Outputs
    # ======================================

    resume_vector_store: Dict[str, Any]

    jd_vector_store: Dict[str, Any]



    # ======================================
    # Retrieval Outputs
    # ======================================

    retrieved_chunks: List[Dict[str, Any]]



    # ======================================
    # Analysis Outputs
    # ======================================

    analysis_result: Dict[str, Any]



    # ======================================
    # Evaluation Metrics
    # ======================================

    evaluation_metrics: Dict[str, Any]



    # ======================================
    # Workflow Status
    # ======================================

    status: str