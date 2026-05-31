# ==========================================
# vector_store_service.py
# Purpose:
# Store semantic embedding vectors inside
# FAISS vector database.
#
# Responsibilities:
# - create FAISS index
# - add embedding vectors
# - store chunk metadata
# - support semantic retrieval
#
# Why This File Exists:
# FAISS enables fast similarity search
# between:
#
# - resume embeddings
# - JD embeddings
#
# This becomes the core retrieval layer
# of the RAG pipeline.
# ==========================================



# ==========================================
# Import Libraries
# ==========================================

import faiss

import numpy as np



# ==========================================
# Function:
# Build FAISS Vector Store
# ==========================================

def build_faiss_index(
    embedded_chunks
):


    # --------------------------------------
    # Empty Embedding List
    # --------------------------------------

    embedding_vectors = []



    # --------------------------------------
    # Store Chunk Metadata
    # --------------------------------------

    chunk_metadata = []



    # --------------------------------------
    # Extract Embedding Vectors
    # --------------------------------------

    for chunk in embedded_chunks:



        # ----------------------------------
        # Store Embedding Vector
        # ----------------------------------

        embedding_vectors.append(

            chunk["embedding"]

        )



        # ----------------------------------
        # Store Metadata
        # ----------------------------------

        chunk_metadata.append({

            "chunk_type": chunk["chunk_type"],

            "content": chunk["content"]

        })



    # --------------------------------------
    # Convert To NumPy Array
    # --------------------------------------

    embedding_array = np.array(

        embedding_vectors,

        dtype="float32"

    )



    # --------------------------------------
    # Get Embedding Dimension
    # --------------------------------------

    embedding_dimension = (
        embedding_array.shape[1]
    )



    # --------------------------------------
    # Create FAISS Index
    # --------------------------------------

    faiss_index = faiss.IndexFlatL2(

        embedding_dimension

    )



    # --------------------------------------
    # Add Embeddings To Index
    # --------------------------------------

    faiss_index.add(

        embedding_array

    )



    # --------------------------------------
    # Return Vector Store
    # --------------------------------------

    return {

        "faiss_index": faiss_index,

        "metadata": chunk_metadata

    }