# Initialization

load_dotenv(override=True)

HF_MODELS = {
    "Qwen 2.5 3B":
        "Qwen/Qwen2.5-3B-Instruct",

    "SmolLM2 1.7B":
        "HuggingFaceTB/SmolLM2-1.7B-Instruct",

    "TinyLlama":
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

    "Phi-3.5 Mini":
        "microsoft/Phi-3.5-mini-instruct"
}

# Sign in to HuggingFace Hub

hf_token = userdata.get('HF_TOKEN')
login(hf_token, add_to_git_credential=True)

system_message = """You are an expert synthetic dataset generator.
Generate realistic and internally consistent datasets.
Always follow the user's requested schema.
Never explain your reasoning.
Return valid JSON only."""
