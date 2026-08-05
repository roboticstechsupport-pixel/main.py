"""
==========================================================
Project ULTRON
AI Assistant Engine
==========================================================
"""

from datetime import datetime

try:
    import ollama
except ImportError:
    ollama = None


class Assistant:
    """
    Core AI Assistant
    """

    def __init__(self, config):

        self.config = config

        self.chat_history = []

        self.system_prompt = {
            "role": "system",
            "content": config.PERSONALITY
        }

        self.chat_history.append(self.system_prompt)

        print("[Assistant] Ready")

    #########################################################

    def initialize(self):

        print(self.config.STARTUP_MESSAGE)

    #########################################################

    def ask(self, message: str) -> str:
        """
        Send a message to the LLM.
        """

        if not message.strip():
            return "Please say something."

        self.chat_history.append(
            {
                "role": "user",
                "content": message
            }
        )

        if self.config.LLM_PROVIDER.lower() == "ollama":
            return self._ask_ollama()

        return "No AI provider configured."

    #########################################################

    def _ask_ollama(self):

        if ollama is None:
            return (
                "The 'ollama' package is not installed.\n"
                "Run:\n"
                "pip install ollama"
            )

        try:

            response = ollama.chat(

                model=self.config.LLM_MODEL,

                messages=self.chat_history

            )

            answer = response["message"]["content"]

            self.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            return answer

        except Exception as e:

            return f"Ollama Error: {e}"

    #########################################################

    def clear_memory(self):

        self.chat_history = [self.system_prompt]

    #########################################################

    def save_chat(self, filename="conversation.txt"):

        with open(filename, "w", encoding="utf-8") as file:

            file.write(
                "ULTRON Conversation Log\n"
            )

            file.write(
                "=" * 40 + "\n"
            )

            file.write(
                f"Date: {datetime.now()}\n\n"
            )

            for msg in self.chat_history:

                role = msg["role"].upper()

                content = msg["content"]

                file.write(
                    f"{role}: {content}\n\n"
                )

        print(f"Conversation saved to {filename}")

    #########################################################

    def shutdown(self):

        print("[Assistant] Shutdown complete.")
