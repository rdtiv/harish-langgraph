# harish-langgraph

This repository is a fork of the original [harishneel1/langgraph](https://github.com/harishneel1/langgraph), a project primarily written in **Jupyter Notebook** (91.3%) and **Python** (8.7%). The original project explores the use of **LangChain** to build dynamic graph-based workflows for tasks involving language models.

## Features
- **Dynamic Graphs**: Leverages the `MessageGraph` class to create workflows for generating and critiquing text.
- **LangChain Integration**: Uses LangChain's prompts and chains for natural language processing tasks.
- **Customizable Chains**: Supports tasks like tweet generation and critique, as seen in the original `chains.py` implementation.
- **Visualization**: Provides functionality to visualize the workflow graph in ASCII or Mermaid.js format.

## How to Use
1. **Setup**:
   - Clone the repository:
     ```bash
     git clone https://github.com/rdtiv/harish-langgraph.git
     cd harish-langgraph
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file with necessary configuration values (e.g., API keys for OpenAI).

2. **Run the Workflow**:
   - Use the provided Python scripts to generate and critique content.
   - Example:
     ```bash
     python 2_basic_reflection_system/basic.py
     ```

## Acknowledgments
This project is based on the original work by [harishneel1](https://github.com/harishneel1/) in the repository [langgraph](https://github.com/harishneel1/langgraph).

## License
Please refer to the original repository's license for terms of use.
