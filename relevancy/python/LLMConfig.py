class LLMConfig:
    """Configuration settings for LLM interactions"""
    api_key = "EMPTY"
    base_url = "http://localhost:9999/v1"
    model = "Llama-3.1-Tulu-3-405B-FP8-Dynamic"
    temperature = 0.0

    logfile = "logfile"

    def __init__(self):
        logger.warn("Warning: LitScanConfig initialized")
        raise Exception("LitScanConfig initialized, please use static vars")
