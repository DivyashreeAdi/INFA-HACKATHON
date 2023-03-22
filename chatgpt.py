secret_key = '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'

#print(prompt)
import openai
openai.api_key = secret_key

def test():
    while True:
        prompt = input()
        output = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = prompt,
            max_tokens= 1000,
            temperature =0
        )

        output_text = output['choices'][0]['text']

        return output_text
    


    #print(output)
