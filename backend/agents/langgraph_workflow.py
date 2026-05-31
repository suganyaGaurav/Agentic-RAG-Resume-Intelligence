# ==========================================
# langgraph_workflow.py
# Purpose:
# Central LangGraph workflow controller.
#
# Responsibilities:
# - register workflow nodes
# - define execution flow
# - pass shared workflow state
# - compile executable workflow
#
# Workflow Pipeline:
#
# Governance
# → Storage
# → Parser
# → Extraction
# → Chunking
# → Embedding
# → Vector Store
# → Retrieval
# → Analysis
# → Evaluation
# ==========================================



# ==========================================
# LangGraph Imports
# ==========================================

from langgraph.graph import (
    StateGraph,
    END
)



# ==========================================
# Shared Workflow State
# ==========================================

from backend.agents.state import (
    ResumeWorkflowState
)



# ==========================================
# Workflow Nodes
# ==========================================

from backend.agents.nodes.governance_node import (
    governance_node
)

from backend.agents.nodes.storage_node import (
    storage_node
)

from backend.agents.nodes.parser_node import (
    parser_node
)

from backend.agents.nodes.extraction_node import (
    extraction_node
)

from backend.agents.nodes.chunking_node import (
    chunking_node
)

from backend.agents.nodes.embedding_node import (
    embedding_node
)

from backend.agents.nodes.vector_store_node import (
    vector_store_node
)

from backend.agents.nodes.retrieval_node import (
    retrieval_node
)

from backend.agents.nodes.analysis_node import (
    analysis_node
)

from backend.agents.nodes.evaluation_node import (
    evaluation_node
)



# ==========================================
# Create Workflow Graph
# ==========================================

workflow = StateGraph(
    ResumeWorkflowState
)



# ==========================================
# Register Workflow Nodes
# ==========================================

workflow.add_node(
    "governance_node",
    governance_node
)

workflow.add_node(
    "storage_node",
    storage_node
)

workflow.add_node(
    "parser_node",
    parser_node
)

workflow.add_node(
    "extraction_node",
    extraction_node
)

workflow.add_node(
    "chunking_node",
    chunking_node
)

workflow.add_node(
    "embedding_node",
    embedding_node
)

workflow.add_node(
    "vector_store_node",
    vector_store_node
)

workflow.add_node(
    "retrieval_node",
    retrieval_node
)

workflow.add_node(
    "analysis_node",
    analysis_node
)

workflow.add_node(
    "evaluation_node",
    evaluation_node
)



# ==========================================
# Workflow Entry Point
# ==========================================

workflow.set_entry_point(
    "governance_node"
)



# ==========================================
# Workflow Execution Order
# ==========================================

workflow.add_edge(
    "governance_node",
    "storage_node"
)

workflow.add_edge(
    "storage_node",
    "parser_node"
)

workflow.add_edge(
    "parser_node",
    "extraction_node"
)

workflow.add_edge(
    "extraction_node",
    "chunking_node"
)

workflow.add_edge(
    "chunking_node",
    "embedding_node"
)

workflow.add_edge(
    "embedding_node",
    "vector_store_node"
)

workflow.add_edge(
    "vector_store_node",
    "retrieval_node"
)

workflow.add_edge(
    "retrieval_node",
    "analysis_node"
)

workflow.add_edge(
    "analysis_node",
    "evaluation_node"
)

workflow.add_edge(
    "evaluation_node",
    END
)



# ==========================================
# Compile Workflow
# ==========================================

app_workflow = workflow.compile()