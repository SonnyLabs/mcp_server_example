from fastmcp import FastMCP
from sonnylabs_py import SonnyLabsClient


mcp = FastMCP("My MCP Server")


from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch values from environment
client = SonnyLabsClient(
    api_token = os.getenv("SONNYLABS_API_TOKEN"),
    analysis_id = os.getenv("SONNYLABS_ANALYSIS_ID"),
    base_url = os.getenv("SONNYLABS_BASE_URL")
)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int, sidenote: str) -> int:
    """Add two numbers with an optional sidenote input (used for prompt injection analysis)."""

    input_result = client.analyze_text(sidenote, scan_type="input")

    print(f"Adding {a} and {b}")
    if sidenote:
        print(f"Sidenote: {sidenote}")

    result = a + b

    output_result = client.analyze_text(str(result), scan_type="output")


    return result

# Start the MCP server
mcp.run()
