# ai-managed-database

DynamoDB MCP Agent using mcp-server-aws and Agno MCP Tools.

## The idea
User enters a natural language query like "Find all orders with status = 'pending'".
The agent uses MCP to translate this into a DynamoDB query. 

This server acts as a bridge between the agent and DynamoDB, allowing the agent to process natural language queries.
