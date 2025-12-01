from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="weather_server")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather for a given location"""
    return f"The weather in {location} is sunny."

if __name__ == "__main__":
    mcp.run(transport="sse")