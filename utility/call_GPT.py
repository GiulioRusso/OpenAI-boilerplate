from openai import OpenAI, OpenAIError


def call_GPT(messages: list,
             model: str) -> None:

    # define OpenAI instance
    openai = OpenAI()

    try:
        # call GPT
        response = openai.chat.completions.create(model=model,
                                                messages=messages)
        
        # print GPT response
        gpt_response = response.choices[0].message.content.strip()
        
        print("\n\t>>> GPT Response: ")
        print(gpt_response)

    except OpenAIError as e:

        print(f"\n\t>>> ERROR: {e.__dict__.get('body')['message']}")