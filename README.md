# Visual AI Chat

> A production-ready vision-based chatbot powered by Qubrid AI's advanced vision models

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/langchain-0.1+-green.svg)](https://langchain.com)

## Overview

Visual AI Chat is an enterprise-grade conversational AI application that enables natural language interactions about images using Qubrid's Qwen3-VL-30B-A3B-Instruct vision model. Built with LangChain and Streamlit, it provides a clean, intuitive interface for vision-based question answering with full conversation history management.

### Key Features

- **Vision-Based Chat**: Ask questions about uploaded images using state-of-the-art vision AI
- **Conversation Management**: Multiple conversation threads with automatic context preservation
- **Streaming Responses**: Real-time token streaming for responsive user experience
- **Model Configuration**: Adjustable temperature, max tokens, top-p, top-k, and presence penalty
- **Memory Management**: LangChain-powered conversation memory with proper context handling
- **Clean Architecture**: Separation of concerns between UI state and model context

## Architecture

```
Visual AI Chat
├── app.py                 # Main application entry point
├── backend/
│   ├── chain.py          # VisionChain orchestration layer
│   ├── qubrid_client.py  # Qubrid API client wrapper
│   ├── prompt.py         # System prompts and templates
│   └── utils.py          # Utility functions
└── frontend/
    ├── ui_components.py  # Sidebar and UI components
    └── base_config.py    # Global UI configuration
```

### Technology Stack

- **Frontend**: Streamlit
- **AI Orchestration**: LangChain
- **Vision Model**: Qubrid Qwen3-VL-30B-A3B-Instruct
- **Image Processing**: Pillow
- **Environment Management**: python-dotenv

## Prerequisites

- Python 3.8 or higher
- Qubrid AI API key ([Get your key](https://qubrid.ai))
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Vision-Chabot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the project root:

```env
QUBRID_API_KEY=your_api_key_here
QUBRID_API_BASE=https://api.qubrid.ai/v1  # Optional, uses default if not set
```

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Basic Workflow

1. **Upload Image**: Click the file uploader and select an image (PNG/JPG)
2. **Ask Questions**: Type your question in the chat input
3. **View Response**: Watch the AI's response stream in real-time
4. **Continue Conversation**: Ask follow-up questions with full context
5. **Manage Conversations**: Switch between conversations or start new ones from the sidebar

### Model Parameters

Adjust these parameters in the sidebar to control model behavior:

- **Temperature** (0.0 - 2.0): Controls randomness. Lower = focused, Higher = creative
- **Max Tokens** (256 - 4096): Maximum response length
- **Top-P** (0.0 - 1.0): Nucleus sampling threshold
- **Top-K** (1 - 100): Number of top tokens to consider
- **Presence Penalty** (-2.0 - 2.0): Penalizes topic repetition

## Project Structure

### Backend Components

#### `backend/chain.py`
- `VisionChain`: Main orchestration class
- Manages LangChain memory integration
- Handles message formatting for Qubrid API
- Provides streaming response interface

#### `backend/qubrid_client.py`
- `QubridVisionLLM`: API client wrapper
- Handles authentication and request formatting
- Manages streaming response parsing
- Error handling and retry logic

#### `backend/prompt.py`
- System prompts for vision understanding
- Configurable prompt templates
- Vision-specific instruction sets

### Frontend Components

#### `frontend/ui_components.py`
- Sidebar rendering (conversations, settings, actions)
- Model parameter controls
- Conversation management UI
- Action buttons (New Chat, Reset Parameters)

#### `frontend/base_config.py`
- Global CSS configuration
- Font and color constants
- Layout constraints
- Theme enforcement

### Main Application

#### `app.py`
- Session state initialization
- Conversation lifecycle management
- Image upload handling
- Chat interface rendering
- Message display and streaming

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `QUBRID_API_KEY` | Yes | - | Your Qubrid AI API key |
| `QUBRID_API_BASE` | No | `https://api.qubrid.ai/v1` | Qubrid API base URL |

### Model Defaults

```python
DEFAULTS = {
    "temperature": 0.7,
    "max_tokens": 1024,
    "top_p": 0.9,
    "top_k": 40,
    "presence_penalty": 0.0
}
```

## API Integration

### Qubrid Vision Model

This application uses Qubrid's Qwen3-VL-30B-A3B-Instruct model via their API:

- **Model**: `Qwen3-VL-30B-A3B-Instruct`
- **Capabilities**: Vision understanding, multi-turn conversation, detailed image analysis
- **Input**: Text + Image (base64 encoded)
- **Output**: Streaming text responses

### Request Format

```python
{
    "model": "Qwen3-VL-30B-A3B-Instruct",
    "messages": [
        {
            "role": "system",
            "content": "System prompt"
        },
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/..."}},
                {"type": "text", "text": "User question"}
            ]
        }
    ],
    "stream": true,
    "temperature": 0.7,
    ...
}
```

## Development

### Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Document functions with docstrings
- Keep functions focused and single-purpose

### Testing

Test the API connection:

```bash
python test_api.py
```

### Debugging

Enable Streamlit debug mode:

```bash
streamlit run app.py --logger.level=debug
```

## Troubleshooting

### Common Issues

**API Key Error**
```
Error: QUBRID_API_KEY not found in environment
```
Solution: Ensure `.env` file exists with valid API key

**Import Error**
```
ModuleNotFoundError: No module named 'langchain_core'
```
Solution: Install dependencies with `pip install -r requirements.txt`

**Image Upload Error**
```
Error: Unsupported image format
```
Solution: Use PNG or JPG images only

## Performance Considerations

- **Image Size**: Large images are automatically resized to optimize API calls
- **Streaming**: Responses stream in real-time for better UX
- **Memory**: Conversation history is stored in session state (cleared on page refresh)
- **Caching**: Streamlit caching is used for static resources

## Security

- API keys are loaded from environment variables (never hardcoded)
- Image data is base64 encoded for secure transmission
- No persistent storage of user data
- Session-based conversation management


## Acknowledgments

- Powered by [Qubrid AI](https://qubrid.ai)
- Built with [LangChain](https://langchain.com)
- UI framework: [Streamlit](https://streamlit.io)

---

**Version**: 1.0.0  
**Last Updated**: January 2026  
**Maintained by**: Qubrid AI

---

Made with ❤️ by Qubrid AI
