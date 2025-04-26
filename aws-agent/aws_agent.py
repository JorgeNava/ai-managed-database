# aws_agent.py
import asyncio, os
from dotenv import load_dotenv
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

load_dotenv()

async def main():
    app = MCPApp(name="aws_resource_agent")
    async with app.run() as _:
        async with Agent(
            name="aws_manager",
            instruction="Gestiona S3 y DynamoDB de forma segura.",
            server_names=["aws"],
        ) as agent:
            llm = await agent.attach_llm(OpenAIAugmentedLLM)
            reply = await llm.generate_str("Lista mis buckets S3")
            print(reply)

if __name__ == "__main__":
    asyncio.run(main())
