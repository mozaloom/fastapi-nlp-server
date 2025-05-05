[![Python application test with Github Actions](https://github.com/mozaloom/fastapi-nlp-server/actions/workflows/main.yml/badge.svg)](https://github.com/mozaloom/fastapi-nlp-server/actions/workflows/main.yml)

# FastAPI NLP Server

A simple API server that leverages Natural Language Processing capabilities using TextBlob and Wikipedia integrations.

## Features

- Wikipedia search functionality
- Text summary extraction from Wikipedia articles
- Noun phrase extraction using TextBlob
- Simple API endpoints for NLP operations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mozaloom/fastapi-nlp-server.git
cd fastapi-nlp-server
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Extract noun phrases from a Wikipedia article:
```bash
python wikiphrases.py "Golden State Warriors"
```

### Python Module

```python
from nlplogic.corenlp import search_wikipedia, get_summary, get_noun_phrases

# Search Wikipedia
results = search_wikipedia("Golden State Warriors")

# Get article summary
summary = get_summary("Golden State Warriors")

# Extract noun phrases
noun_phrases = get_noun_phrases("Golden State Warriors")
```

## Testing

Run the test suite:
```bash
python -m pytest test_corenlp.py
```

## Project Structure

```
.
├── LICENSE
├── Makefile
├── README.md
├── nlplogic/           # Core NLP logic package
│   ├── __init__.py
│   └── corenlp.py      # NLP functions using TextBlob and Wikipedia
├── requirements.txt    # Project dependencies
├── test_corenlp.py     # Unit tests
└── wikiphrases.py      # CLI tool for noun phrase extraction
```

## Dependencies

- TextBlob - For natural language processing tasks
- Wikipedia - For accessing Wikipedia content
- Fire - For creating command line interfaces
- pytest - For testing

## License

See the [LICENSE](LICENSE) file for details.