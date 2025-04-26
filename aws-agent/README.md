# MCP + AWS Starter Kit (S3 & DynamoDB)

## 0. Requisitos
* **pyenv** (gestiona versiones de Python)
* **Node ≥ 18** (para `mcp-server-aws`)
* AWS IAM user con permisos RW sobre S3 y DynamoDB

## 1. Instalación
```bash
pyenv install 3.12.3 && pyenv virtualenv 3.12.3 mcp-aws
pyenv local mcp-aws

pip install -r requirements.txt
cp .env.example .env             # y completa tus claves

npm install -g @smithery/cli
smithery install mcp-server-aws   # instala el servidor MCP
