# ==========================================
# chunking_service.py
# Purpose:
# Convert structured extraction JSON into
# contextual semantic competency chunks
# for RAG retrieval.
#
# Responsibilities:
# - create semantic chunks
# - preserve competency categories
# - preserve contextual meaning
# - improve embedding quality
# - ignore empty categories
# - prepare richer retrieval inputs
#
# Why This File Exists:
# Instead of:
# naive keyword chunking
#
# This project now uses:
#
# "contextual semantic chunking"
#
# This improves:
# - retrieval realism
# - semantic grounding
# - retrieval accuracy
# - explainability
# - recruiter relevance
# - hallucination reduction
# ==========================================



# ==========================================
# Context Templates
# Purpose:
# Add semantic meaning around extracted
# skills before embeddings are generated.
# ==========================================

CONTEXT_TEMPLATES = {

    "ai_skills": (

        "Experienced in building and "
        "working with AI systems using "

    ),

    "backend_skills": (

        "Built backend services and APIs "
        "using "

    ),

    "cloud_skills": (

        "Worked with cloud infrastructure "
        "and deployment technologies like "

    ),

    "deployment_skills": (

        "Experience deploying scalable "
        "production systems using "

    ),

    "evaluation_skills": (

        "Implemented evaluation, "
        "observability, governance, and "
        "AI validation workflows using "

    ),

    "operations_skills": (

        "Handled operational workflows "
        "and infrastructure processes using "

    ),

    "leadership_skills": (

        "Provided leadership, mentoring, "
        "and team collaboration involving "

    ),

    "training_skills": (

        "Delivered training and knowledge "
        "sharing sessions involving "

    ),

    "experience": (

        "Professional experience includes "

    ),

    "required_experience": (

        "Role requires professional "
        "experience of "

    ),

    "education": (

        "Educational background includes "

    ),

    "certifications": (

        "Certified and trained in "

    ),

    "role_domain": (

        "Target role focuses on "

    )

}



# ==========================================
# Function:
# Create Semantic Chunks
# ==========================================

def create_semantic_chunks(

    structured_json

):


    # --------------------------------------
    # Store Generated Chunks
    # --------------------------------------

    semantic_chunks = []



    # --------------------------------------
    # Process Each Category
    # --------------------------------------

    for category, values in structured_json.items():



        # ----------------------------------
        # Skip Empty Categories
        # ----------------------------------

        if not values:

            continue



        # ----------------------------------
        # Convert List Into Text
        # ----------------------------------

        values_text = " ".join(values)



        # ----------------------------------
        # Fetch Context Template
        # ----------------------------------

        context_prefix = (

            CONTEXT_TEMPLATES.get(

                category,

                "Relevant experience includes "

            )

        )



        # ----------------------------------
        # Build Contextual Chunk
        # ----------------------------------

        contextual_chunk = (

            context_prefix

            +

            values_text

        )



        # ----------------------------------
        # Create Semantic Chunk
        # ----------------------------------

        chunk = {

            "chunk_type": category,

            "content": contextual_chunk

        }



        # ----------------------------------
        # Store Chunk
        # ----------------------------------

        semantic_chunks.append(
            chunk
        )



    # --------------------------------------
    # Return Semantic Chunks
    # --------------------------------------

    return semantic_chunks