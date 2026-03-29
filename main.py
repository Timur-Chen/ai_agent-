from agent import Agent
from memory import MemoryManager
from tool_registry import ToolRegistry

# Import tools
from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.translator_tool import TranslatorTool
from tools.weather_tool import WeatherTool


def main():
    # Initialize registry and register tools
    registry = ToolRegistry()

    registry.register("calculator", CalculatorTool())
    registry.register("get_time", TimeTool())
    registry.register("translate", TranslatorTool())
    registry.register("get_weather", WeatherTool())

    # Initialize memory
    memory = MemoryManager()

    # Create agent
    agent = Agent(registry, memory)

    # Run agent
    agent.run()


if __name__ == "__main__":
    main()