from tools.base_tool import BaseTool


class WeatherTool(BaseTool):
    """
    A simple weather tool (mock implementation).
    """

    def execute(self, city: str):
        """
        Returns weather information for a given city.

        Args:
            city (str): City name

        Returns:
            str: Weather information (simulated)
        """
        try:
            # Mock weather data (for assignment purposes)
            return f"The weather in {city} is sunny, 25°C"
        except Exception as e:
            return f"Weather error: {str(e)}"

    def get_declaration(self) -> dict:
        """
        Returns schema for Gemini function calling.
        """
        return {
            "name": "get_weather",
            "description": "Get weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }