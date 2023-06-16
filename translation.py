""" The following code is intended as a demo to send the input from user into the poe api, 
not for merchantability or any other commercial use """

import poe
client = poe.Client("TOKEN-HERE")

def get_response(message):
  response =""
  for chunk in client.send_message("chinchilla", message):
    response += (chunk["text_new"])
  return response

def clear_context():
  client.send_chat_break("chinchilla")



def translate(input_language, output_language, input_text):
    clear_context()
    if input_language == "Detect Language":
        input_language = "the language of the text you are translating"
    prompt = f"""
    your task is to translate the text delimited by triple backticks from {input_language} to {output_language}:
    only return the translated text, not the quotation marks or any other preamble or postscript
    ```{input_text}```
    """
    response = get_response(prompt)
    return response



