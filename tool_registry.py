from typing import Dict
from tools.base_tool import BaseTool


class ToolRegistry:
    """
    Registry for managing and executing tools.

    This class follows the Factory/Registry pattern.
    It allows dynamic registration and retrieval of tools
    without modifying the Agent class.
    """

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register(self, tool_name: str, tool: BaseTool):
        """
        Registers a new tool in the registry.

        Args:
            tool_name (str): Name of the tool.
            tool (BaseTool): Tool instance
        """
        self.tools[tool_name] = tool

    def get_tool(self, tool_name: str) -> BaseTool | None:
        """
        Retrieves a tool by name.

        Args:
            tool_name (str): Name of the tool

        Returns:
            BaseTool or None
        """
        return self.tools.get(tool_name)

    def execute_tool(self, tool_name: str, **kwargs):
        """
        Executes a tool safely with error handling.

        Args:
            tool_name (str): Name of the tool
            **kwargs: Arguments for the tool

        Returns:
            Result of execution or error message
        """
        tool = self.get_tool(tool_name)

        if not tool:
            return f"Error: Tool '{tool_name}' not found."

        try:
            return tool.execute(**kwargs)
        except Exception as e:
            return f"Error executing tool '{tool_name}': {str(e)}"

    def get_all_declarations(self):
        """
        Returns all tool schemas for Gemini function calling.

        Returns:
            List of tool declarations
        """
        return [tool.get_declaration() for tool in self.tools.values()]