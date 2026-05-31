# ==========================================
# retrieval_service.py
# Purpose:
# Perform semantic similarity retrieval
# using FAISS vector search.
#
# Responsibilities:
# - query FAISS vector database
# - retrieve top matching chunks
# - calculate similarity scores
# - return semantic matches
#
# Why This File Exists:
# This service acts as the:
# "semantic search engine"
#
# It enables:
# JD requirements
# → semantic resume matching
# ==========================================



# ==========================================
# Import Libraries
# ==========================================

import numpy as np



# ==========================================
# Function:
# Retrieve Semantic Matches
# ==========================================

def retrieve_semantic_matches(

    jd_embeddings,

    resume_vector_store,

    top_k=1

):


    # --------------------------------------
    # Extract FAISS Index
    # --------------------------------------

    faiss_index = (

        resume_vector_store["faiss_index"]

    )



    # --------------------------------------
    # Extract Resume Metadata
    # --------------------------------------

    resume_metadata = (

        resume_vector_store["metadata"]

    )



    # --------------------------------------
    # Store Retrieval Results
    # --------------------------------------

    retrieval_results = []



    # --------------------------------------
    # Process Each JD Embedding
    # --------------------------------------

    for jd_chunk in jd_embeddings:



        # ----------------------------------
        # Convert Query Embedding
        # ----------------------------------

        query_embedding = np.array(

            [jd_chunk["embedding"]],

            dtype="float32"

        )



        # ----------------------------------
        # Perform FAISS Search
        # ----------------------------------

        distances, indices = faiss_index.search(

            query_embedding,

            top_k

        )



        # ----------------------------------
        # Process Retrieved Matches
        # ----------------------------------

        for distance, index in zip(

            distances[0],

            indices[0]

        ):



            # --------------------------------
            # Get Resume Match
            # --------------------------------

            matched_chunk = (

                resume_metadata[index]

            )



            # --------------------------------
            # Convert Distance To Similarity
            # --------------------------------

            similarity_score = float(

                1 / (1 + distance)

            )



            # --------------------------------
            # Store Retrieval Result
            # --------------------------------

            retrieval_results.append({

                "query_chunk_type": (

                    jd_chunk["chunk_type"]

                ),

                "query_content": (

                    jd_chunk["content"]

                ),

                "matched_chunk_type": (

                    matched_chunk["chunk_type"]

                ),

                "matched_content": (

                    matched_chunk["content"]

                ),

                "similarity_score": round(

                    similarity_score,

                    4

                )

            })



    # --------------------------------------
    # Return Retrieval Results
    # --------------------------------------

    return retrieval_results