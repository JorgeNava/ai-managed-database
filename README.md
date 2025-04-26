# Saphira

DynamoDB MCP Agent using mcp-server-aws and Agno MCP Tools.

## The idea
User enters a natural language query like "Find all orders with status = 'pending'".
The agent uses MCP to translate this into a DynamoDB query. 

This server acts as a bridge between the agent and DynamoDB, allowing the agent to process natural language queries.


## Example commands
- Crea una nueva tabla llamada Notas con campos para la nota, la fecha en que fue creada y la fecha en que actualizada por ultima vez.

## Referenes
### Articles
- https://dev.to/aws-builders/querying-dynamodb-with-natural-language-using-mcp-5c4c
- https://dev.to/aws/hype-or-hope-is-mcp-the-missing-piece-of-the-llm-puzzle-c88
- https://github.com/rishikavikondala/mcp-server-aws

### Repositories
- https://github.com/rishikavikondala/mcp-server-aws
- https://github.com/imankamyabi/dynamodb-mcp-server