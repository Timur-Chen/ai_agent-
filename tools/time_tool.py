from datetime import datetime
from tools.base_tool import BaseTool


class TimeTool(BaseTool):
    """
    A tool to get the current system time.
    """

    def execute(self):
        """
        Returns the current time.

        Returns:
            str: Current time in readable format
        """
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def get_declaration(self) -> dict:
        """
        Returns schema for Gemini function calling.
        """
        return {
            "name": "get_time",
            "description": "Get the current system time",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }