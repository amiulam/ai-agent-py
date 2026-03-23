# AI Agent Python (ai-agent-py)

An autonomous AI agent powered by Google's Gemini model (via `google-genai`) that can interact with the local file system and execute Python code. This project demonstrates a tool-calling loop where the LLM can browse files, read content, write new files, and run scripts to solve complex tasks.

## Features

- **Autonomous Tool Use**: Uses Gemini's function calling to interact with the environment.
- **File System Operations**:
    - `get_files_info`: List files and directory structures.
    - `get_file_content`: Read the contents of specific files.
    - `write_file`: Create or update files on disk.
- **Code Execution**:
    - `run_python_file`: Execute Python scripts locally and capture stdout/stderr.
- **Iterative Reasoning**: Implements a multi-turn conversation loop (up to 20 iterations) to allow the agent to refine its actions based on tool outputs.

## Tech Stack

- **Language**: Python >= 3.13
- **LLM**: Google Gemini
- **Environment Management**: `uv` (recommended) or `pip`
- **Configuration**: `python-dotenv` for API key management

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-agent-py
   ```

2. **Install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_ai_studio_api_key_here
   ```

## Usage

Run the agent by passing a prompt as a command-line argument:

```bash
python main.py "Analyze the files in the calculator directory and fix any bugs you find in the tests."
```

### Options
- `--verbose`: Enable detailed logging of function calls, tool responses, and token usage.

## Project Structure

- `main.py`: Entry point containing the orchestration loop and LLM configuration.
- `call_function.py`: Logic for mapping LLM function calls to local Python functions.
- `functions/`: Directory containing the individual tool implementations (read, write, list, run).
- `prompts.py`: Defines the system instruction that guides the agent's behavior.
- `calculator/`: A sample workspace for the agent to demonstrate its capabilities.

## Security Note

This agent has the capability to **execute code** (`run_python_file`) and **write files** on your local system. Always run it in a controlled environment and be cautious when providing prompts that might lead to destructive actions.

## License

This project is open source and available for educational purposes.