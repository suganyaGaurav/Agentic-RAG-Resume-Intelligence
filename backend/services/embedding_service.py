# ==========================================
# embedding_service.py
# Purpose:
# Generate semantic embeddings for
# structured competency chunks.
#
# Responsibilities:
# - load embedding model
# - generate embeddings
# - attach embeddings to chunks
# - prepare vector-ready outputs
#
# Why This File Exists:
# This service converts semantic chunk
# text into numerical vector embeddings
# for:
#
# - FAISS similarity search
# - semantic retrieval
# - competency matching
# ==========================================



# ==========================================
# Import Sentence Transformer
# ==========================================

from sentence_transformers import (
    SentenceTransformer
)



# ==========================================
# Load Embedding Model
# ==========================================

embedding_model = SentenceTransformer(

    "sentence-transformers/all-MiniLM-L6-v2"

)



# ==========================================
# Function:
# Generate Chunk Embeddings
# ==========================================

def generate_chunk_embeddings(
    semantic_chunks
):


    # --------------------------------------
    # Store Embedded Chunks
    # --------------------------------------

    embedded_chunks = []



    # --------------------------------------
    # Process Each Chunk
    # --------------------------------------

    for chunk in semantic_chunks:



        # ----------------------------------
        # Extract Chunk Content
        # ----------------------------------

        chunk_content = chunk["content"]



        # ----------------------------------
        # Generate Embedding Vector
        # ----------------------------------

        embedding_vector = embedding_model.encode(

            chunk_content

        ).tolist()



        # ----------------------------------
        # Create Embedded Chunk
        # ----------------------------------

        embedded_chunk = {

            "chunk_type": chunk["chunk_type"],

            "content": chunk_content,

            "embedding": embedding_vector

        }



        # ----------------------------------
        # Store Embedded Chunk
        # ----------------------------------

        embedded_chunks.append(

            embedded_chunk

        )



    # --------------------------------------
    # Return Embedded Chunks
    # --------------------------------------

    return embedded_chunks