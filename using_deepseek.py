from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.deepseek.com"
) 

def inference(user_input):
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input},
        ],
        stream=False,
        reasoning_effort="low",
        extra_body={"thinking": {"type":"disabled"}}
    )
    output = response.choices[0].message.content
    return output

while True:
    user_input = input("User: ")
    print("Bot: ", inference(user_input))
