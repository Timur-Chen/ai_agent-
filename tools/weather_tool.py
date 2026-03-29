from tools.base_tool import BaseTool


class WeatherTool(BaseTool):

    def execute(self, city: str):
        # Always return Riga weather (static)
        return "The weather in Riga is cloudy, 10°C"

    def get_declaration(self) -> dict:
        return {
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }