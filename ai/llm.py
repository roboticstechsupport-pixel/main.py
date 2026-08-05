"""
==========================================================
Project ULTRON
ai/llm.py
==========================================================
"""

from typing import List, Dict

try:
    import ollama
except ImportError:
    ollama = None


class LLMClient:

    def __init__(self, config):

        self.config = config

        self.provider = config.LLM_PROVIDER.lower()

        self.model = config.LLM_MODEL

    ##########################################################

    def generate(self, messages: List[Dict]) -> str:

        if self.provider == "ollama":
            return self._ollama(messages)

        raise ValueError(
            f"Unsupported provider: {self.provider}"
        )

    ##########################################################

    def stream(self, messages):

        if self.provider != "ollama":
            raise ValueError("Streaming not supported.")

        if ollama is None:
            raise ImportError(
                "Install the ollama package first."
            )

        stream = ollama.chat(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:

            if "message" in chunk:

                yield chunk["message"]["content"]

    ##########################################################

    def _ollama(self, messages):

        if ollama is None:
            raise ImportError(
                "pip install ollama"
            )

        response = ollama.chat(

            model=self.model,

            messages=messages

        )

        return response["message"]["content"]

    ##########################################################

    def available_models(self):

        if ollama is None:
            return []

        try:

            models = ollama.list()

            return [
                model["model"]
                for model in models["models"]
            ]

        except Exception:

            return []

    ##########################################################

    def change_model(self, model_name):

        self.model = model_name
