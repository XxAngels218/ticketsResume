from dotenv import load_dotenv
import os

import openai

load_dotenv()
prompt = os.getenv("PROMPT")

openai.api_key = os.getenv("API_KEY")
text = os.getenv("TEXT")


def make_summary(text=text, prompt=prompt):
    prompt_parts = [prompt[i:i+1201] for i in range(0, len(prompt), 1201)]
    response = ""

    for part in prompt_parts:
        completion = openai.Completion.create(engine="text-davinci-003",
                                              prompt=text + part,
                                              max_tokens=2048 - len(response))
        response += completion.choices[0].text

    response_parts = response.split("Solution:")
    problem = response_parts[0].replace("Problem:", "")
    solution = "".join(response_parts[1:]).replace("Solution:", "")
    summary = [problem, solution]

    return summary
