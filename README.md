# MCP Streamlit Chatbot

This repository is meant as a hands-on practice of working with MCP in a Streamlit chatbot that is meant to be deployed in AWS.

## Project Structure

```
mcp-streamlit-chatbot/
├── app/                    # Streamlit application
│   ├── main.py            # Main Streamlit application file
│   ├── mcp_client.py      # MCP client implementation
│   └── tools/             # Application-specific tools
├── data/                  # Data directory for PDFs and other files
│   └──
├── docker/                # Docker configuration files
│   ├── docker-compose.yml # Container orchestration
│   ├── Dockerfile.app     # Streamlit app container
│   └── Dockerfile.mcp     # MCP server container
├── mcp-server/           # MCP server implementation
│   ├── main.py           # MCP server entry point
│   └── tools/            # MCP server tools
│       └── summarize_pdf.py
├── Makefile              # Build and deployment commands
└── requirements.txt      # Python dependencies
```

## Prerequisites

- Docker and Docker Compose
- Make (optional, for using Makefile commands)

## Setup and Running

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp-streamlit-chatbot
   ```

2. Build and start the containers:
   ```bash
   make build
   make up
   ```

3. Access the applications:
   - Streamlit App: http://localhost:8501
   - MCP Server: http://localhost:8000

## Available Make Commands

The project includes a Makefile with the following commands:

```bash
make help      # Show all available commands
make build     # Build the containers
make up        # Start containers in detached mode
make down      # Stop and remove containers
make ps        # List running containers
make logs      # Show logs from all containers
make up-logs   # Start containers in foreground mode (with logs)
make clean     # Remove all containers, images, and volumes
make rebuild   # Rebuild and restart containers
make restart   # Restart containers
```

### Service-Specific Commands

```bash
# Show logs for a specific service
make service-logs SERVICE=streamlit-app

# Execute a command in a container
make exec SERVICE=streamlit-app CMD=bash
```

## Development

The application consists of two main components:

1. **Streamlit App** (`app/`):
   - Provides the chat interface
   - Communicates with the MCP server
   - Handles user interactions

2. **MCP Server** (`mcp-server/`):
   - Implements the MCP protocol
   - Provides tools for PDF processing
   - Handles backend operations

## Data Directory

The `data/` directory is mounted to both containers:
- Streamlit App: `/app/data`
- MCP Server: `/mcp/data`

Place any PDFs or other files you want to process in this directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License


