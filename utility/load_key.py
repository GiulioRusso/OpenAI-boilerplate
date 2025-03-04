import os

from dotenv import load_dotenv
from utility.check_key import check_key


def load_key(debug: bool = False) -> None:
    """
    Loads the OpenAI API key from the .env file.

    :param debug: Debug flag.
    """

    # load key from .env file
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')

    # check API key
    check_key(api_key=api_key,
              debug=debug)
