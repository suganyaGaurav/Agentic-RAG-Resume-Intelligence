# ==========================================
# evaluation_service.py
# Purpose:
# Evaluate retrieval quality, scoring
# consistency, and semantic matching
# reliability for the AI Resume Match System.
#
# Responsibilities:
# - evaluate retrieval quality
# - measure semantic match strength
# - count strong/partial/weak matches
# - validate score consistency
# - prepare evaluation metrics
#
# Why This File Exists:
# Before introducing LLM generation,
# deterministic evaluation must validate:
#
# - retrieval reliability
# - scoring realism
# - semantic grounding
#
# This improves:
# - explainability
# - observability
# - governance confidence
# - AI trustworthiness
# ==========================================



# ==========================================
# Function:
# Evaluate Retrieval Quality
# ==========================================

def evaluate_retrieval_quality(

    analysis_result,

    retrieval_results

):


    # --------------------------------------
    # Empty Safety Validation
    # --------------------------------------

    if not retrieval_results:


        return {

            "evaluation_status": (
                "FAILED"
            ),

            "retrieval_precision": 0,

            "strong_match_count": 0,

            "partial_match_count": 0,

            "missing_skill_count": 0,

            "score_consistency": (
                "UNSTABLE"
            ),

            "evaluation_summary": (
                "No retrieval results available "
                "for evaluation."
            )

        }



    # --------------------------------------
    # Extract Match Groups
    # --------------------------------------

    strong_matches = (
        analysis_result.get(
            "strong_matches",
            []
        )
    )



    partial_matches = (
        analysis_result.get(
            "partial_matches",
            []
        )
    )



    missing_skills = (
        analysis_result.get(
            "missing_skills",
            []
        )
    )



    # --------------------------------------
    # Count Match Categories
    # --------------------------------------

    strong_match_count = len(
        strong_matches
    )



    partial_match_count = len(
        partial_matches
    )



    missing_skill_count = len(
        missing_skills
    )



    # --------------------------------------
    # Calculate Retrieval Precision
    # --------------------------------------

    total_meaningful_matches = (

        strong_match_count

        +

        partial_match_count

    )



    total_results = len(
        retrieval_results
    )



    retrieval_precision = round(

        (

            total_meaningful_matches

            /

            total_results

        )

        * 100,

        2

    )



    # --------------------------------------
    # Score Consistency Validation
    # --------------------------------------

    overall_score = (
        analysis_result.get(
            "overall_score",
            0
        )
    )



    # --------------------------------------
    # Simple Consistency Logic
    # --------------------------------------

    if overall_score >= 70:

        score_consistency = (
            "HIGH_ALIGNMENT"
        )



    elif overall_score >= 50:

        score_consistency = (
            "MODERATE_ALIGNMENT"
        )



    else:

        score_consistency = (
            "LOW_ALIGNMENT"
        )



    # --------------------------------------
    # Evaluation Status
    # --------------------------------------

    if retrieval_precision >= 70:

        evaluation_status = (
            "GOOD"
        )



    elif retrieval_precision >= 50:

        evaluation_status = (
            "MODERATE"
        )



    else:

        evaluation_status = (
            "WEAK"
        )



    # --------------------------------------
    # Evaluation Summary
    # --------------------------------------

    evaluation_summary = (

        f"Retrieval precision is "

        f"{retrieval_precision}% with "

        f"{strong_match_count} strong "

        f"matches and "

        f"{partial_match_count} partial "

        f"matches."

    )



    # --------------------------------------
    # Return Evaluation Metrics
    # --------------------------------------

    return {

        "evaluation_status": (
            evaluation_status
        ),

        "retrieval_precision": (
            retrieval_precision
        ),

        "strong_match_count": (
            strong_match_count
        ),

        "partial_match_count": (
            partial_match_count
        ),

        "missing_skill_count": (
            missing_skill_count
        ),

        "score_consistency": (
            score_consistency
        ),

        "evaluation_summary": (
            evaluation_summary
        )

    }