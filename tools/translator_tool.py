from tools.base_tool import BaseTool
from deep_translator import GoogleTranslator


class TranslatorTool(BaseTool):

    def execute(self, text: str, target_language: str):
        try:
            translated = GoogleTranslator(
                source='auto',
                target=target_language
            ).translate(text)

            return translated

        except Exception as e:
            return f"Translation error: {str(e)}"

    def get_declaration(self) -> dict:
        return {
            "name": "translate",
            "description": "Translate text into a specified language",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "target_language": {"type": "string"}
                },
                "required": ["text", "target_language"]
            }
        }