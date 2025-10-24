# Build Your Own Local MCP Client with LlamaIndex

A comprehensive demonstration of building a **local MCP (Model Context Protocol) client** using LlamaIndex. This project enables you to connect to local MCP servers and interact with them using natural language through powerful tool-calling agents—all running entirely on your local machine.

## 🚀 Overview

This project showcases:
- **Local MCP Client** implementation using LlamaIndex
- **Tool-calling agents** that can interact with various MCP servers
- **Multiple LLM backend support** (OpenAI-compatible and Ollama)
- **SQLite integration** through MCP protocol for natural language database queries
- **Local-first architecture** ensuring privacy and offline capability

## 📋 Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- Ollama (if using Ollama backend)
- Local LLM setup (if using OpenAI-compatible local server)

## ⚡ Quick Start

### 1. Install Dependencies

```sh
uv sync
```

### 2. Start the MCP Server

Launch the local SQLite MCP server:

```sh
uv run server.py --server_type=sse
```

### 3. Run the Client

Choose the client that matches your LLM backend:

**For OpenAI-compatible models:**
```sh
uv run client.py
```

**For Ollama models:**
```sh
uv run ollama_client.py
```

### 4. Interact with the Agent

Once running, type your natural language queries in the terminal. The agent will intelligently use the available tools to answer your questions.

## 🛠️ Project Structure

```
.
├── client.py              # OpenAI-compatible client
├── ollama_client.py       # Ollama-specific client
├── server.py             # MCP server implementation
├── pyproject.toml        # Project dependencies
└── README.md            # This file
```

## 🔧 Configuration

### Server Types
The MCP server supports different transport protocols:
- `sse` - Server-Sent Events (recommended)
- `stdio` - Standard input/output

### Environment Variables
Configure your LLM endpoints through environment variables or direct configuration in the client files.

## 💡 Example Usage

Once everything is running, you can ask questions like:

- "Show me all users in the database"
- "What's the average age of customers?"
- "Find orders placed in the last week"

The agent will automatically use the available SQLite tools through the MCP protocol to execute these queries and return natural language responses.

## 🔍 How It Works

1. **MCP Server**: Exposes tools (like SQLite database operations) through the Model Context Protocol
2. **MCP Client**: Connects to the server and discovers available tools
3. **LlamaIndex Agent**: Uses tool-calling capabilities to interpret natural language and execute appropriate tools
4. **Local LLM**: Processes queries and generates responses using your local language model

## 🐛 Troubleshooting

- Ensure your MCP server is running before starting the client
- Verify your LLM endpoint is accessible and properly configured
- Check that all dependencies are installed with `uv sync`
- For SQLite issues, ensure the database file exists and is accessible

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This project is designed for local development and experimentation with MCP protocols and local LLM agents.