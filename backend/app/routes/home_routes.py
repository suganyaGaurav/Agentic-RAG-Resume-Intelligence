# ==========================================
# home_routes.py
# Purpose:
# Main application routes for the
# Governance-Aware Resume Match System.
#
# Responsibilities:
# - render homepage
# - receive uploaded files
# - initialize workflow state
# - invoke LangGraph workflow
# - render workflow outputs
# - handle workflow errors
# ==========================================



# ==========================================
# Flask Imports
# ==========================================

from flask import (

    Blueprint,

    render_template,

    request,

    flash

)



# ==========================================
# LangGraph Workflow
# ==========================================

from backend.agents.langgraph_workflow import (
    app_workflow
)



# ==========================================
# Initialize Blueprint
# ==========================================

home_blueprint = Blueprint(

    "home_blueprint",

    __name__

)



# ==========================================
# Home Route
# ==========================================

@home_blueprint.route(

    "/",

    methods=["GET", "POST"]

)

def home():



    # ======================================
    # Handle POST Request
    # ======================================

    if request.method == "POST":


        try:


            # ----------------------------------
            # Receive Uploaded Files
            # ----------------------------------

            resume_file = request.files.get(
                "resume_file"
            )

            jd_file = request.files.get(
                "jd_file"
            )



            # ----------------------------------
            # Initialize Workflow State
            # ----------------------------------

            initial_state = {


                # ------------------------------
                # Uploaded Files
                # ------------------------------

                "resume_file": resume_file,

                "jd_file": jd_file,



                # ------------------------------
                # Saved File Paths
                # ------------------------------

                "resume_path": "",

                "jd_path": "",



                # ------------------------------
                # Parsed Text
                # ------------------------------

                "resume_text": "",

                "jd_text": "",



                # ------------------------------
                # Masked Governance-Safe Text
                # ------------------------------

                "masked_resume_text": "",

                "masked_jd_text": "",



                # ------------------------------
                # Structured Extraction Output
                # ------------------------------

                "resume_json": {},

                "jd_json": {},



                # ------------------------------
                # Workflow Observability
                # ------------------------------

                "workflow_logs": [],

                "error_message": "",



                # ------------------------------
                # Chunking Outputs
                # ------------------------------

                "resume_chunks": [],

                "jd_chunks": [],



                # ------------------------------
                # Embedding Outputs
                # ------------------------------

                "resume_embeddings": [],

                "jd_embeddings": [],



                # ------------------------------
                # Vector Store Outputs
                # ------------------------------

                "resume_vector_store": {},

                "jd_vector_store": {},



                # ------------------------------
                # Retrieval Outputs
                # ------------------------------

                "retrieved_chunks": [],



                # ------------------------------
                # Analysis Outputs
                # ------------------------------

                "analysis_result": {},



                # ------------------------------
                # Evaluation Metrics
                # ------------------------------

                "evaluation_metrics": {},



                # ------------------------------
                # Workflow Status
                # ------------------------------

                "status": "workflow_started"

            }



            # ----------------------------------
            # Invoke Workflow
            # ----------------------------------

            final_state = app_workflow.invoke(

                initial_state

            )



            # ----------------------------------
            # Analysis Results
            # ----------------------------------

            formatted_analysis_results = (

                final_state["analysis_result"]

            )



            # ----------------------------------
            # Evaluation Results
            # ----------------------------------

            formatted_evaluation_results = (

                final_state["evaluation_metrics"]

            )



            # ----------------------------------
            # Render Success UI
            # ----------------------------------

            return render_template(

                "index.html",

                success_message=(

                    "Workflow completed successfully"

                ),

                analysis_results=(

                    formatted_analysis_results

                ),

                evaluation_results=(

                    formatted_evaluation_results

                ),

                workflow_logs=(

                    final_state["workflow_logs"]

                )

            )



        except Exception as error:


            # ----------------------------------
            # Flash Workflow Error
            # ----------------------------------

            flash(

                f"error::{str(error)}"

            )



            # ----------------------------------
            # Render Error UI
            # ----------------------------------

            return render_template(

                "index.html"

            )



    # ======================================
    # Default Homepage
    # ======================================

    return render_template(

        "index.html"

    )