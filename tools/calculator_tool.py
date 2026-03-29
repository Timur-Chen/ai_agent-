from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    """
    A simple calculator tool to evaluate mathematical expressions.
    """

    def execute(self, expression: str):
        """
        Evaluates a mathematical expression.

        Args:
            expression (str): Math expression (e.g., "2+2")

        Returns:
            str: Result of calculation
        """
        try:
            # WARNING: eval is used for simplicity (acceptable for assignment)
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculation error: {str(e)}"

    def get_declaration(self) -> dict:
        """
        Returns schema for Gemini function calling.
        """
        return {
            "name": "calculator",
            "description": "Evaluate mathematical expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }