# TamilAI

A command-line AI assistant that responds in Tamil using OpenAI's API.

## Installation

### Using Poetry (Recommended)

```bash
poetry install
```

### Using pip

```bash
pip install -r requirements.txt
```

## Usage

```bash
# If installed with Poetry
tamilai "your question here"

# If installed with pip
python -m tamilai.cli "your question here"
```

## Requirements

```bash
- Python 3.9 or higher
- OpenAI API key
```

## Example

```bash
tamilai "How are you?"
# Will respond with Tamil text
```

## Features

- Natural Tamil language responses
- Command-line interface
- Powered by OpenAI's GPT models
- Context-aware conversations

## Configuration

1. Get an OpenAI API key from https://platform.openai.com/
2. Create a `.env` file and add:
```
OPENAI_API_KEY=your_api_key_here
```

## License

MIT License