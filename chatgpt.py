secret_key = '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'

import openai
from flask import Flask

openai.api_key = secret_key
app = Flask(__name__)

@app.route('/')
def test():
    while True :
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
    app.debug=True
    app.run()

