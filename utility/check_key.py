import sys

def check_key(api_key: str,
              debug: bool) -> None:
    """
    Checks the validity of the API key.

    :param api_key: The API key to validate.
    :param debug: Debug flat.
    """

    if not api_key:
        print("!!! ERROR: No API key was found. Please check the .env file and make sure the API key is specified as 'OPENAI_API_KEY=sk-proj-...' ")
        sys.exit(1)
    elif not api_key.startswith("sk-proj-"):
        print("!!! ERROR: API key was found, but it doesn't start 'sk-proj-'. Please check you're using the right key in the .env file ")
        sys.exit(1)
    elif api_key.strip() != api_key:
        print("!!! ERROR: API key was found, but it looks like it might have space or tab characters at the start or end. Please remove them")
        sys.exit(1)
    else:
        if debug:
            print("--> DEBUG: API key found!") 
