# ==========================================
# Intelligence Service
# Purpose:
# Handle all resume intelligence processing
# before matching and scoring.
#
# Responsibilities:
# - Mask sensitive PII data
# - Extract structured resume information
# - Extract structured JD information
# - Detect competency categories
# - Normalize ATS-style role patterns
# - Support future semantic matching
#
# Note:
# This acts as the core AI intelligence
# layer of the governance-aware system.
# ==========================================


# ==========================================
# Import Required Libraries
# ==========================================

import re



# ==========================================
# Function:
# Remove Duplicate Values
# ==========================================

def remove_duplicates(items):

    cleaned_items = []


    for item in items:

        if item not in cleaned_items:

            cleaned_items.append(item)


    return cleaned_items



# ==========================================
# Function:
# Mask PII Information
# ==========================================

def mask_pii_data(text):

    # --------------------------------------
    # Mask Email Addresses
    # --------------------------------------

    text = re.sub(

        r'[\w\.-]+@[\w\.-]+\.\w+',

        '[EMAIL_MASKED]',

        text

    )


    # --------------------------------------
    # Mask Phone Numbers
    # --------------------------------------

    text = re.sub(

        r'(\+?\d[\d\-\s]{8,}\d)',

        '[PHONE_MASKED]',

        text

    )


    # --------------------------------------
    # Mask LinkedIn URLs
    # --------------------------------------

    text = re.sub(

        r'linkedin\.com\/\S+',

        '[LINKEDIN_MASKED]',

        text,

        flags=re.IGNORECASE

    )


    # --------------------------------------
    # Mask GitHub URLs
    # --------------------------------------

    text = re.sub(

        r'github\.com\/\S+',

        '[GITHUB_MASKED]',

        text,

        flags=re.IGNORECASE

    )


    return text



# ==========================================
# Function:
# Detect Skills From Category
# ==========================================

def detect_skills(text, keywords):

    detected_skills = []


    for keyword in keywords:

        if keyword.lower() in text.lower():

            detected_skills.append(keyword)


    return remove_duplicates(
        detected_skills
    )



# ==========================================
# Function:
# Extract Resume Information
# ==========================================

def extract_resume_information(text):

    extracted_data = {

        "ai_skills": [],

        "backend_skills": [],

        "cloud_skills": [],

        "deployment_skills": [],

        "leadership_skills": [],

        "evaluation_skills": [],

        "operations_skills": [],

        "experience": [],

        "education": [],

        "certifications": [],

        "projects": []

    }


    # ======================================
    # AI Skills
    # ======================================

    ai_keywords = [

        "LLM",
        "RAG",
        "LangChain",
        "LangGraph",
        "OpenAI",
        "Anthropic",
        "Gemini",
        "Prompt Engineering",
        "Transformers",
        "BERT",
        "Hugging Face",
        "PyTorch",
        "TensorFlow",
        "Deep Learning",
        "Machine Learning",
        "Generative AI",
        "FAISS",
        "Whisper",
        "LoRA",
        "QLoRA",
        "PEFT"

    ]


    extracted_data["ai_skills"] = (
        detect_skills(text, ai_keywords)
    )


    # ======================================
    # Backend Skills
    # ======================================

    backend_keywords = [

        "Python",
        "FastAPI",
        "Flask",
        "REST APIs",
        "API",
        "PostgreSQL",
        "Micro-services",
        "Node.js"

    ]


    extracted_data["backend_skills"] = (
        detect_skills(text, backend_keywords)
    )


    # ======================================
    # Cloud Skills
    # ======================================

    cloud_keywords = [

        "AWS",
        "Azure",
        "GCP",
        "Lambda",
        "Cloud Deployment"

    ]


    extracted_data["cloud_skills"] = (
        detect_skills(text, cloud_keywords)
    )


    # ======================================
    # Deployment Skills
    # ======================================

    deployment_keywords = [

        "Docker",
        "CI/CD",
        "Kubernetes",
        "GitHub Actions",
        "MLOps",
        "Deployment"

    ]


    extracted_data["deployment_skills"] = (
        detect_skills(
            text,
            deployment_keywords
        )
    )


    # ======================================
    # Leadership Skills
    # ======================================

    leadership_keywords = [

        "Mentored",
        "Leadership",
        "Trainer",
        "Training",
        "Mentoring",
        "Stakeholder",
        "Project Management",
        "Team Leadership",
        "Coaching"

    ]


    extracted_data["leadership_skills"] = (
        detect_skills(
            text,
            leadership_keywords
        )
    )


    # ======================================
    # Evaluation Skills
    # ======================================

    evaluation_keywords = [

        "Evaluation",
        "Benchmarking",
        "AI Validation",
        "Observability",
        "Testing",
        "Quality",
        "Governance",
        "Bias",
        "Risk Assessment"

    ]


    extracted_data["evaluation_skills"] = (
        detect_skills(
            text,
            evaluation_keywords
        )
    )


    # ======================================
    # Operations Skills
    # ======================================

    operations_keywords = [

        "Linux",
        "Unix",
        "Networking",
        "Cisco",
        "Operations",
        "Infrastructure"

    ]


    extracted_data["operations_skills"] = (
        detect_skills(
            text,
            operations_keywords
        )
    )


    # ======================================
    # Experience Extraction
    # ======================================

    experience_matches = re.findall(

        r'\d+\+?\s+years',

        text,

        flags=re.IGNORECASE

    )


    extracted_data["experience"] = (
        remove_duplicates(
            experience_matches
        )
    )


    # ======================================
    # Education Extraction
    # ======================================

    education_keywords = [

        "B.E.",
        "B.Tech",
        "MBA",
        "PG Diploma",
        "Computer Science",
        "Artificial Intelligence",
        "Machine Learning",
        "MTech",
        "Electronics",
        "Communication"

    ]


    extracted_data["education"] = (
        detect_skills(
            text,
            education_keywords
        )
    )


    # ======================================
    # Certification Extraction
    # ======================================

    certification_keywords = [

        "AWS",
        "AI Security",
        "NVIDIA",
        "Bloomberg",
        "Azure",
        "Google Cloud"

    ]


    extracted_data["certifications"] = (
        detect_skills(
            text,
            certification_keywords
        )
    )


    # ======================================
    # Project Extraction
    # ======================================

    project_patterns = [

        r'End-to-End AI Dubbing Platform',

        r'Intelligent Book Recommendation System',

        r'Conversational AI Assistants',

        r'LLM Optimization & Fine-Tuning',

        r'Scalable AI Microservices',

        r'AI Security & Governance Implementation'

    ]


    detected_projects = []


    for pattern in project_patterns:

        if pattern.lower() in text.lower():

            detected_projects.append(pattern)


    extracted_data["projects"] = (
        remove_duplicates(
            detected_projects
        )
    )


    return extracted_data



# ==========================================
# Function:
# Extract JD Information
# ==========================================

def extract_jd_information(text):

    extracted_data = {

        "role_domain": [],

        "ai_skills": [],

        "backend_skills": [],

        "cloud_skills": [],

        "deployment_skills": [],

        "leadership_skills": [],

        "training_skills": [],

        "evaluation_skills": [],

        "operations_skills": [],

        "required_experience": []

    }


    # ======================================
    # Role Domain Detection
    # ======================================

    role_domains = {

        "AI_ENGINEERING": [

            "LLM",
            "RAG",
            "LangChain",
            "GenAI",
            "Prompt Engineering"

        ],

        "AI_TRAINING": [

            "Trainer",
            "Mentor",
            "Teaching",
            "Learners",
            "Training"

        ],

        "AI_EVALUATION": [

            "Evaluation",
            "Benchmarking",
            "Metrics",
            "JSON",
            "Role-play"

        ],

        "OPERATIONS_MANAGEMENT": [

            "Linux",
            "Unix",
            "Operations",
            "Infrastructure",
            "Networking"

        ]

    }


    for domain, keywords in role_domains.items():

        for keyword in keywords:

            if keyword.lower() in text.lower():

                extracted_data["role_domain"].append(
                    domain
                )

                break


    # ======================================
    # AI Skills
    # ======================================

    ai_keywords = [

        "LLM",
        "RAG",
        "LangChain",
        "LangGraph",
        "Prompt Engineering",
        "Embeddings",
        "Vector Search",
        "OpenAI",
        "Anthropic",
        "Gemini",
        "LoRA",
        "QLoRA",
        "PEFT",
        "Hugging Face"

    ]


    extracted_data["ai_skills"] = (
        detect_skills(text, ai_keywords)
    )


    # ======================================
    # Backend Skills
    # ======================================

    backend_keywords = [

        "FastAPI",
        "Flask",
        "REST APIs",
        "API",
        "Database",
        "Frontend",
        "React",
        "Node.js"

    ]


    extracted_data["backend_skills"] = (
        detect_skills(
            text,
            backend_keywords
        )
    )


    # ======================================
    # Cloud Skills
    # ======================================

    cloud_keywords = [

        "AWS",
        "Azure",
        "GCP",
        "Cloud"

    ]


    extracted_data["cloud_skills"] = (
        detect_skills(
            text,
            cloud_keywords
        )
    )


    # ======================================
    # Deployment Skills
    # ======================================

    deployment_keywords = [

        "Docker",
        "CI/CD",
        "Deployment",
        "Containerization",
        "GitHub Actions",
        "MLOps"

    ]


    extracted_data["deployment_skills"] = (
        detect_skills(
            text,
            deployment_keywords
        )
    )


    # ======================================
    # Leadership Skills
    # ======================================

    leadership_keywords = [

        "Leadership",
        "Mentor",
        "Coaching",
        "Team Management",
        "Stakeholder",
        "Project Management"

    ]


    extracted_data["leadership_skills"] = (
        detect_skills(
            text,
            leadership_keywords
        )
    )


    # ======================================
    # Training Skills
    # ======================================

    training_keywords = [

        "Trainer",
        "Training",
        "Teaching",
        "Learners",
        "Curriculum",
        "Learning Sessions"

    ]


    extracted_data["training_skills"] = (
        detect_skills(
            text,
            training_keywords
        )
    )


    # ======================================
    # Evaluation Skills
    # ======================================

    evaluation_keywords = [

        "Evaluation",
        "Benchmarking",
        "Metrics",
        "JSON",
        "Instruction Adherence",
        "Role-play"

    ]


    extracted_data["evaluation_skills"] = (
        detect_skills(
            text,
            evaluation_keywords
        )
    )


    # ======================================
    # Operations Skills
    # ======================================

    operations_keywords = [

        "Linux",
        "Unix",
        "Networking",
        "Cisco",
        "Infrastructure",
        "Operations"

    ]


    extracted_data["operations_skills"] = (
        detect_skills(
            text,
            operations_keywords
        )
    )


    # ======================================
    # Experience Extraction
    # ======================================

    experience_matches = re.findall(

        r'\d+\+?\s+years',

        text,

        flags=re.IGNORECASE

    )


    extracted_data["required_experience"] = (
        remove_duplicates(
            experience_matches
        )
    )


    return extracted_data