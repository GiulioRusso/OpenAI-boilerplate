import openai

def print_response(response: openai.Stream):
    """
    Print GPT response with typewriter effect

    :param response: OpenAI Stream object
    """
    
    print("\n>>> ", end='')

    for chunk in response:
        content = chunk.choices[0].delta.content or ''
        print(content, end='', flush=True)  # print each chunk as it arrives
