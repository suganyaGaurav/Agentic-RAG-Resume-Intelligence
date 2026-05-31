# ==========================================
# analysis_service.py
# Purpose:
# Analyze semantic retrieval results and
# generate governed AI match intelligence.
#
# Responsibilities:
# - calculate weighted match score
# - prioritize critical AI competencies
# - identify strong matches
# - identify partial matches
# - identify weak/missing skills
# - determine support eligibility
# - prepare AI-ready analysis output
#
# Why This File Exists:
# Retrieval gives:
# raw semantic matches
#
# This service converts them into:
# business intelligence
#
# Improvements Added:
# - weighted scoring
# - role-aware prioritization
# - better recruiter realism
# ==========================================



# ==========================================
# Skill Weight Configuration
# ==========================================

SKILL_WEIGHTS = {

    "ai_skills": 1.5,

    "deployment_skills": 1.4,

    "cloud_skills": 1.3,

    "evaluation_skills": 1.3,

    "backend_skills": 1.1,

    "operations_skills": 1.1,

    "required_experience": 1.5,

    "leadership_skills": 0.7,

    "training_skills": 0.5,

    "education": 0.6,

    "certifications": 0.8

}



# ==========================================
# Function:
# Analyze Retrieval Results
# ==========================================

def analyze_retrieval_results(

    retrieval_results

):


    # --------------------------------------
    # Empty Retrieval Protection
    # --------------------------------------

    if not retrieval_results:


        return {

            "overall_score": 0,

            "support_level": "NO_SUPPORT",

            "strong_matches": [],

            "partial_matches": [],

            "missing_skills": [],

            "recommendation": (
                "No semantic matches found"
            )

        }



    # --------------------------------------
    # Initialize Variables
    # --------------------------------------

    weighted_scores = []

    total_weight = 0

    strong_matches = []

    partial_matches = []

    missing_skills = []



    # --------------------------------------
    # Process Retrieval Results
    # --------------------------------------

    for result in retrieval_results:



        # ----------------------------------
        # Extract Similarity Score
        # ----------------------------------

        score = (
            result["similarity_score"]
        )



        # ----------------------------------
        # Extract Chunk Type
        # ----------------------------------

        chunk_type = (
            result["query_chunk_type"]
        )



        # ----------------------------------
        # Get Weight
        # ----------------------------------

        weight = SKILL_WEIGHTS.get(

            chunk_type,

            1.0

        )



        # ----------------------------------
        # Weighted Score Calculation
        # ----------------------------------

        weighted_score = (
            score * weight
        )



        weighted_scores.append(
            weighted_score
        )



        total_weight += weight



        # ----------------------------------
        # Strong Match Detection
        # ----------------------------------

        if score >= 0.70:


            strong_matches.append({

                "query": (
                    result["query_content"]
                ),

                "matched": (
                    result["matched_content"]
                ),

                "score": score

            })



        # ----------------------------------
        # Partial Match Detection
        # ----------------------------------

        elif score >= 0.50:


            partial_matches.append({

                "query": (
                    result["query_content"]
                ),

                "matched": (
                    result["matched_content"]
                ),

                "score": score

            })



        # ----------------------------------
        # Weak / Missing Skills
        # ----------------------------------

        else:


            missing_skills.append({

                "query": (
                    result["query_content"]
                ),

                "score": score

            })



    # --------------------------------------
    # Weighted Average Calculation
    # --------------------------------------

    weighted_average = (

        sum(weighted_scores)

        /

        total_weight

    )



    # --------------------------------------
    # Convert To Percentage
    # --------------------------------------

    overall_score = round(

        weighted_average * 100,

        2

    )



    # --------------------------------------
    # Determine Support Level
    # --------------------------------------

    if overall_score < 60:


        support_level = (
            "LOW_SUPPORT"
        )



        recommendation = (

            "Current profile has limited "
            "alignment with this role. "
            "Focus on strengthening missing "
            "technical competencies before "
            "resume optimization."

        )



    elif overall_score < 80:


        support_level = (
            "MEDIUM_SUPPORT"
        )



        recommendation = (

            "Profile shows moderate alignment. "
            "Improving missing skills and "
            "project depth may significantly "
            "increase role compatibility."

        )



    else:


        support_level = (
            "HIGH_SUPPORT"
        )



        recommendation = (

            "Profile strongly aligns with the "
            "target role. Resume enhancement "
            "guidance can now be safely "
            "provided."

        )



    # --------------------------------------
    # Return Analysis Output
    # --------------------------------------

    return {

        "overall_score": overall_score,

        "support_level": support_level,

        "strong_matches": strong_matches,

        "partial_matches": partial_matches,

        "missing_skills": missing_skills,

        "recommendation": recommendation

    }