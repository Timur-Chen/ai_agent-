from memory import MemoryManager
from tool_registry import ToolRegistry


class Agent:
    """
    Mock AI Agent (used due to API quota limitations)
    Simulates reasoning and tool usage.
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

            # 🔹 Calculator
            if any(op in user_input for op in ["+", "-", "*", "/"]):
                result = self.registry.execute_tool(
                    "calculator",
                    expression=user_input
                )
                print(f"Assistant: {result}")

            # 🔹 Time
            elif "time" in user_lower:
                result = self.registry.execute_tool("get_time")
                print(f"Assistant: {result}")

            # 🔹 Translation (FINAL FIXED)
            elif "translate" in user_lower or " in " in user_lower:
                try:
                    text = ""
                    target_language = ""

                    if "translate" in user_lower:
                        # format: translate hello to spanish
                        cleaned = user_input.lower().replace("translate", "").strip()

                        if "to" in cleaned:
                            text_part, lang_part = cleaned.split("to", 1)
                            text = text_part.strip()
                            target_language = lang_part.strip()

                    elif " in " in user_lower:
                        # format: hello in spanish
                        text_part, lang_part = user_input.lower().split(" in ", 1)
                        text = text_part.strip()
                        target_language = lang_part.strip()

                    if not text:
                        text = "hello"
                    if not target_language:
                        target_language = "english"

                    result = self.registry.execute_tool(
                        "translate",
                        text=text,
                        target_language=target_language
                    )

                    print(f"Assistant: {result}")

                except Exception:
                    print("Assistant: Translation failed.")

            # 🔹 Weather
            elif "weather" in user_lower:
                try:
                    words = user_input.split()

                    if "in" in words:
                        city = words[words.index("in") + 1]
                    else:
                        city = "Tashkent"

                    result = self.registry.execute_tool(
                        "get_weather",
                        city=city
                    )

                    print(f"Assistant: {result}")

                except Exception:
                    print("Assistant: Weather fetch failed.")

            # 🔹 Default
            else:
                print("Assistant: I can help with calculations, time, translation, and weather.")