# ReAct Agentic AI

A ReAct (Reasoning + Acting) AI agent built with LangGraph that can perform multi-step reasoning tasks by using tools like web search and weather APIs.

## Overview

This project implements an intelligent agent that can:
- Search the web for information using DuckDuckGo
- Fetch real-time weather data for any city
- Chain multiple operations together to answer complex queries
- Show step-by-step reasoning and actions

The agent uses the **ReAct pattern**, which allows it to reason about a problem, decide which tools to use, execute actions, and observe results before proceeding.

## Features

- 🤖 **GPT-4o Powered**: Uses OpenAI's GPT-4o model for advanced reasoning
- 🔍 **Web Search**: Integrated DuckDuckGo search for finding information
- 🌤️ **Weather Data**: Custom tool to fetch current weather from Weatherstack API
- 🔄 **Multi-Step Reasoning**: Can break down complex queries into multiple steps
- 📊 **Streaming Output**: Real-time display of agent's thought process

## Prerequisites

- Python 3.9 or higher
- OpenAI API key
- Weatherstack API key (optional, for weather functionality)

## Installation

1. Clone or navigate to the project directory:
```bash
cd AiAgent
```

2. Install required dependencies:
```bash
pip install langchain-openai langchain-community langgraph python-dotenv requests
```

Or create a `requirements.txt`:
```txt
langchain-openai
langchain-community
langgraph
python-dotenv
requests
```

Then install:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project directory with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
WEATHERSTACK_API_KEY=your_weatherstack_api_key_here
```

### Getting API Keys

- **OpenAI API Key**: Sign up at [platform.openai.com](https://platform.openai.com) and create an API key
- **Weatherstack API Key**: Sign up at [weatherstack.com](https://weatherstack.com) (free tier available)

## Usage

Run the agent:

```bash
python reActAgenticAI.py
```

The agent will process the query: *"Find the capital of Madhya Pradesh, then find its current weather condition."*

You can modify the query in the code (line 43) to ask different questions.

### Example Queries

- "What is the population of Tokyo, and what's the weather there?"
- "Find the latest news about AI, then check the weather in San Francisco"
- "What is the capital of France and its current temperature?"

## How It Works

1. **Tool Definition**: The agent has access to two tools:
   - `DuckDuckGoSearchRun`: For searching the web
   - `get_weather_data`: Custom tool for fetching weather information

2. **Agent Creation**: Uses LangGraph's `create_react_agent` which implements the ReAct pattern:
   - **Reasoning**: The agent thinks about what to do
   - **Acting**: It selects and uses appropriate tools
   - **Observing**: It processes the tool results
   - **Iterating**: It continues until the query is answered

3. **Streaming**: The agent streams its responses, showing step-by-step reasoning and actions in real-time.

## Project Structure

```
AiAgent/
├── reActAgenticAI.py    # Main agent implementation
└── .env                  # Environment variables (create this)
```

## Dependencies

- `langchain-openai`: OpenAI integration for LangChain
- `langchain-community`: Community tools (DuckDuckGo search)
- `langgraph`: For building stateful, multi-actor applications
- `python-dotenv`: For loading environment variables
- `requests`: For making HTTP requests to weather API

## Customization

### Adding New Tools

You can add custom tools by decorating functions with `@tool`:

```python
@tool
def your_custom_tool(param: str) -> str:
    """Description of what your tool does."""
    # Your tool logic here
    return result

# Add to tools list
tools = [search_tool, get_weather_data, your_custom_tool]
```

### Changing the Model

Modify line 35 to use a different model:

```python
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)  # Cheaper option
```

## Troubleshooting

- **"No module named 'langchain_openai'"**: Install dependencies with `pip install -r requirements.txt`
- **"API key not found"**: Ensure your `.env` file exists and contains valid API keys
- **Weather API errors**: Check that your Weatherstack API key is valid and you haven't exceeded rate limits

## License

This project is for educational purposes.

## Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Uses [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- Weather data provided by [Weatherstack](https://weatherstack.com)

