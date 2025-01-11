from openai import OpenAI, OpenAIError
from utility.debug_print import debug_print
from utility.print_response import print_response



def call_GPT(messages: list,
             model: str,
             debug: bool = False) -> None:
    """
    Call the OpenAI API to query the model. Print the response content.

    :param messages: input message in the OpenAI API format.
    :param model: GPT model.
    :param debug: Debug flag.
    """

    # define OpenAI instance
    openai = OpenAI()

    try:
        # debug print
        if debug:
            debug_print(messages=messages, model=model)

        # call GPT
        response = openai.chat.completions.create(model=model,
                                                  messages=messages,
                                                  stream=True)

        # print GPT response
        print_response(response=response)


    except OpenAIError as e:

        print(f"\n\t!!! ERROR: {e.__dict__.get('body')['message']}")