import re
from memory import MemoryManager
from tool_registry import ToolRegistry


class Agent:
    """
    Smart Mock Agent with Riga-specific time & weather
    """

    def __init__(self, registry: ToolRegistry, memory: MemoryManager):
        self.registry = registry
        self.memory = memory

    def run(self):
        print("🤖 AI Agent started (Mock Mode). Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                break

            self.memory.add_message("user", user_input)
            user_lower = user_input.lower()

            response = ""

            # 🔹 Calculator
            if any(op in user_input for op in ["+", "-", "*", "/"]):
                try:
                    expression = re.findall(r"[0-9\+\-\*\/\.]+", user_input)
                    expression = "".join(expression)

                    response = self.registry.execute_tool(
                        "calculator",
                        expression=expression
                    )
                except:
                    response = "Calculation failed."

            # 🔹 TIME → Riga only
            elif "time" in user_lower:
                response = self.registry.execute_tool("get_time")

            # 🔹 WEATHER → Riga only
            elif "weather" in user_lower:
                response = self.registry.execute_tool(
                    "get_weather",
                    city="Riga"
                )

            # 🔹 TRANSLATION
            elif "translate" in user_lower or " in " in user_lower:
                try:
                    text = ""
                    target_language = ""

                    if "translate" in user_lower:
                        cleaned = user_input.lower().replace("translate", "").strip()

                        if "to" in cleaned:
                            text_part, lang_part = cleaned.split("to", 1)
                            text = text_part.strip().replace("'", "").replace('"', "")
                            target_language = lang_part.strip()

                    elif " in " in user_lower:
                        text_part, lang_part = user_input.lower().split(" in ", 1)
                        text = text_part.strip().replace("'", "").replace('"', "")
                        target_language = lang_part.strip()

                    if not text:
                        text = "hello"
                    if not target_language:
                        target_language = "english"

                    response = self.registry.execute_tool(
                        "translate",
                        text=text,
                        target_language=target_language
                    )

                except:
                    response = "Translation failed."

            # 🔹 DEFAULT
            else:
                response = "I can help with calculations, time, translation, and weather."

            print(f"Assistant: {response}")