import openai
openai.api_key = "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"


def make_summary(cadena, prompt):
    prompt_parts = [prompt[i:i+1201] for i in range(0, len(prompt), 1201)]
    response = ""

    for part in prompt_parts:
        completion = openai.Completion.create(engine="text-davinci-003",
                                              prompt=cadena + part,
                                              max_tokens=2048 - len(response))
        response += completion.choices[0].text

    response_parts = response.split("Solution:")
    problem = response_parts[0].replace("Problem:", "")
    solution = "".join(response_parts[1:]).replace("Solution:", "")
    summary = [problem, solution]

    return summary
