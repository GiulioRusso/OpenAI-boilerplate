# OpenAI Boilerplate Project

Boilerplate for working with the OpenAI API.

## Structure

```
OpenAI-boilerplate/
├── prompts/               # Folder containing prompt text files
│   ├── system_prompt.txt  # System prompt content
│   ├── user_prompt.txt    # User prompt content
├── utility/               # Utility scripts
│   ├── build_messages.py  # Builds messages for the OpenAI API
│   ├── call_GPT.py        # Handles API calls to OpenAI
│   ├── check_key.py       # Validates the API key
│   ├── debug_print.py     # Prints debug information
│   ├── indent_prompt.py   # Formats text with indentation
│   ├── load_key.py        # Loads the API key from .env
│   ├── read_file.py       # Reads content from text files
├── .env                   # Environment file (API key)
├── .gitignore             # Git ignore file
├── main.py                # Main script to run the project
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
```

## Prerequisites
1. Python 3.8+
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Setting Up the Project

### Step 1: Create the `.env` File
The `.env` file is used to store your OpenAI API key. You can create it inside the project folder via the command line:

```bash
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```
Replace `sk-your-api-key-here` with your actual OpenAI API key.

### Step 2: Fill the `prompts/` Directory
Ensure that the `prompts/` folder contains the following files:
- `system_prompt.txt`: A text file with the system prompt.
- `user_prompt.txt`: A text file with the user prompt.

You can modify these files to suit your use case.

### Step 3: Run the Main Script
Run the `main.py` script with custom file paths and model names as parameters:

```bash
python3 main.py
--system_prompt ./prompts/system_prompt.txt
--user_prompt ./prompts/user_prompt.txt
--model gpt-4o-mini
```

## Utility Scripts
- **`load_key.py`**: Loads the API key from the `.env` file.
- **`read_file.py`**: Reads and returns the content of a text file.
- **`build_messages.py`**: Constructs message objects for the OpenAI API.
- **`debug_print.py`**: Displays debugging information.
- **`call_GPT.py`**: Sends the constructed messages to the OpenAI API and retrieves the response.
- **`check_key.py`**: Validates the API key format.
- **`indent_prompt.py`**: Adds indentation to the text content for formatting.

## Troubleshooting
- **No API Key Found**: Ensure your `.env` file is correctly set up with the `OPENAI_API_KEY` variable.
- **File Not Found Errors**: Verify that the paths to `system_prompt.txt` and `user_prompt.txt` are correct.
- **Dependency Issues**: Run `pip3 install -r requirements.txt` to install all required dependencies.

## License
This project is open-source and available under the MIT License.

