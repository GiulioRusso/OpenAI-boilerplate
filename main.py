import argparse
from utility.load_key import load_key
from utility.display_init_terminal import display_init_terminal
from utility.read_prompt import read_prompt
from utility.build_messages import build_messages
from utility.call_GPT import call_GPT

def main(system_prompt_path: str, model: str) -> None:

    # load API key from .env file
    load_key(debug=True)

    # load the welcome print
    display_init_terminal()
                                                                                       
    # build the message for the OpenAI API
    messages = build_messages(
        system_prompt=read_prompt(file_path=system_prompt_path),
        user_prompt=input(">>> ")
    )

    # call OpenAI API
    call_GPT(messages=messages, model=model, debug=True)


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(description="Run GPT-4 with specified prompts and model.")
    
    # define command-line arguments
    parser.add_argument('--system_prompt', type=str, required=True, 
                        help="Path to the system prompt text file.")
    parser.add_argument('--model', type=str, required=True, 
                        help="The model string to use (e.g., 'gpt-4o-mini').")
    
    # parse the arguments
    args = parser.parse_args()

    # run the main function with the parsed arguments
    main(system_prompt_path=args.system_prompt, 
         model=args.model)