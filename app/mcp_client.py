import requests
import os

MCP_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")

def call_tool(tool_name: str, tool_args: dict) -> str:
    try:
        endpoint = f"{MCP_URL}/tools/{tool_name}"
        response = requests.post(endpoint, json=tool_args)
        if response.status_code == 200:
            return response.json().get("result", "No result key returned.")
        return f"Error calling tool: {response.text}"
    except Exception as e:
        return f"Exception occurred while calling MCP tool: {e}"
