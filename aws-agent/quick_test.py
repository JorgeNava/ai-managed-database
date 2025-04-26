# quick_test.py
import asyncio
from dotenv import load_dotenv 
from mcp_agent.app import MCPApp
from mcp_agent.mcp.gen_client import gen_client

load_dotenv() 

async def test():
    async with MCPApp(name="tmp").run() as app:
      async with gen_client("aws", app.server_registry) as aws:
        buckets = await aws.call_tool("s3_bucket_list", arguments={})
        tools = await aws.list_tools()
        print(tools)
        print("Buckets:", buckets)

asyncio.run(test())
