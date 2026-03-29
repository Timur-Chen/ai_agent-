from typing import List, Dict


class MemoryManager:
    """
    Manages conversation history for the agent.

    This class is responsible only for storing and retrieving
    messages, following the Single Responsibility Principle (SRP).
    """

    def __init__(self):
        self.history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        """
        Adds a message to the conversation history.

        Args:
            role (str): 'user', 'assistant', or 'tool'
            content (str): Message content
        """
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self) -> List[Dict[str, str]]:
        """
        Returns full conversation history.

        Returns:
            List of messages
        """
        return self.history

    def clear(self):
        """
        Clears the conversation history.
        """
        self.history = []