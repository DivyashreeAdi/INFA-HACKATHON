import openai
from flask import Flask
import os

openai.api_key = os.environ['secret_key']
app = Flask(__name__)

@app.route('/')
def test():
    prompt = input("Enter your prompt: ")
    output = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        temperature=0
    )
    output_text = output['choices'][0]['text']
    return output_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


