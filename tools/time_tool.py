from tools.base_tool import BaseTool
from datetime import datetime
import pytz


class TimeTool(BaseTool):

    def execute(self):
        try:
            riga_tz = pytz.timezone("Europe/Riga")
            current_time = datetime.now(riga_tz)

            return current_time.strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            return f"Time error: {str(e)}"

    def get_declaration(self) -> dict:
        return {
            "name": "get_time",
            "description": "Get current time in Riga",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }