from abc import ABC, abstractmethod


class BaseTool(ABC):
    @abstractmethod
    def execute(self, **kwargs):
        """
        Executes the tool logic.

        Args:
            **kwargs: Parameters required for the tool

        Returns:
            Result of the tool execution
        """
        pass

    @abstractmethod
    def get_declaration(self) -> dict:
        """
        Returns the function declaration (JSON schema)
        required for Gemini function calling.

        Returns:
            dict: Tool schema definition
        """
        pass