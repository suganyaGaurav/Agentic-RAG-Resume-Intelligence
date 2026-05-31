# Agentic-RAG-Resume-Intelligence

## Overview

Agentic-RAG-Resume-Intelligence is a Governance-Aware Agentic RAG workflow system designed to intelligently analyze resumes against job descriptions using LangGraph orchestration, semantic retrieval pipelines, structured competency extraction, and evaluation-first AI engineering principles.

This project moves beyond traditional ATS keyword matching systems by combining:

* LangGraph workflow orchestration
* Retrieval-Augmented Generation (RAG)
* Semantic embeddings + FAISS vector retrieval
* Structured resume intelligence extraction
* Governance-aware validation pipelines
* Explainable AI workflow execution
* Evaluation-driven AI engineering

The system is intentionally designed as a modular AI workflow architecture rather than a simple chatbot or keyword-based ATS clone.

---

# Core Features

* Resume + JD PDF upload workflow
* Governance-aware validation layer
* PDF parsing using PyMuPDF
* PII masking pipeline
* Structured competency extraction
* Role-domain intelligence extraction
* LangGraph workflow orchestration
* Modular node-based AI pipeline
* Semantic retrieval architecture
* Evaluation-first workflow design

---

# Technology Stack

## Backend

* Python
* Flask

## Workflow Orchestration

* LangGraph
* LangChain

## RAG Pipeline

* Sentence Transformers
* FAISS

## PDF Processing

* PyMuPDF

## Evaluation Frameworks

* LangSmith
* RAGAS
* DeepEval

---

# Current Workflow Architecture

```plaintext
Upload PDFs
      ↓
Governance Validation
      ↓
Storage Layer
      ↓
PDF Parsing
      ↓
PII Masking
      ↓
Competency Extraction
      ↓
Structured JSON Output
```

---

# Planned Agentic RAG Workflow

```plaintext
START
  ↓
Governance Node
  ↓
Storage Node
  ↓
Parser Node
  ↓
Extraction Node
  ↓
Chunking Node
  ↓
Embedding Node
  ↓
Retrieval Node
  ↓
Analysis Node
  ↓
Evaluation Node
  ↓
END
```

---

# Project Structure

```plaintext
AI_Resume_match/

│
├── app.py
├── requirements.txt
│
├── frontend/
│
├── uploads/
│
├── backend/
│   │
│   ├── agents/
│   │   ├── state.py
│   │   ├── langgraph_workflow.py
│   │   └── nodes/
│   │
│   ├── services/
│   │   ├── governance_service.py
│   │   ├── parser_service.py
│   │   ├── intelligence_service.py
│   │   ├── storage_service.py
│   │   └── cleanup_service.py
│   │
│   ├── rag/
│   ├── evaluation/
│   ├── utils/
│   ├── memory/
│   └── logs/
│
├── tests/
├── data/
├── docs/
└── notebooks/
```

---

# LangGraph Architecture

This project uses a clean separation between:

## Services

Reusable business logic.

Examples:

* PDF parsing
* competency extraction
* governance validation

## Nodes

LangGraph workflow wrappers that orchestrate services.

Example:
Parser Node → calls parser_service.py

This architecture keeps the system:

* modular
* reusable
* scalable
* evaluation-friendly

---

# RAG Architecture

The RAG pipeline is designed for:

* semantic resume retrieval
* JD retrieval
* grounded match analysis
* contextual recommendation generation

The system uses:

* Sentence Transformers for embeddings
* FAISS for local vector storage
* Retrieval pipelines for grounded AI workflows

---

# Evaluation-First Design

A major focus of this project is AI workflow evaluation and observability.

## LangSmith

Used for:

* tracing
* workflow observability
* node execution tracking

## RAGAS

Used for:

* context precision
* faithfulness
* retrieval evaluation

## DeepEval

Used for:

* hallucination detection
* groundedness evaluation
* output correctness validation

---

# Engineering Focus

This project emphasizes:

* Governance-aware AI systems
* Modular AI architecture
* Explainable workflows
* Evaluation-first engineering
* Agentic orchestration
* Retrieval grounding
* Workflow observability

instead of building a simple resume keyword matcher.

---

# Future Enhancements

* Semantic chunking
* Embedding pipelines
* FAISS retrieval workflows
* Match scoring engine
* Explainability layer
* Evaluation dashboards
* Agentic recommendation workflows

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

---

# Repository Purpose

This repository was built as a practical hands-on implementation of:

* LangGraph workflows
* RAG systems
* AI evaluation pipelines
* Governance-aware AI engineering
* Agentic orchestration patterns

for learning, experimentation, and portfolio demonstration.

