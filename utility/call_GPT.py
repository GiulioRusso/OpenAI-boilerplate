from openai import OpenAI, OpenAIError
from IPython.display import Markdown, display, update_display


def call_GPT(messages: list,
             model: str) -> None:
    """
    Call the OpenAI API to query the model. Print the response content.

    :param messages: input message in the OpenAI API format.
    """

    # define OpenAI instance
    openai = OpenAI()

    try:
        # call GPT
        response = openai.chat.completions.create(model=model,
                                                messages=messages,
                                                stream=True)
        
        # print GPT response
        print("\n\t>>> GPT Response: ")

        for chunk in response:
            content = chunk.choices[0].delta.content or ''
            print(content, end='', flush=True)  # print each chunk as it arrives

    except OpenAIError as e:

        print(f"\n\t>>> ERROR: {e.__dict__.get('body')['message']}")