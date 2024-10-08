### Pre-requisite
 * [asdf](https://asdf-vm.com/)
 * python 3.12
 * [poetry](https://python-poetry.org/)
 * [ollama](https://ollama.com/)

### Environment setup
```bash
brew install asdf ollama python@3.12
pip install poetry
# or use asdf to manage a base python!
export POETRY_VIRTUALENVS_IN_PROJECT=true
python -m poetry update
# this will setup a virtual environment .venv in project directory
```

### Running the chat UI
```bash
. ./venv/bin/activate
streamlit run ./llm_chat.py
```
