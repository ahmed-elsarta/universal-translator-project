""" The following code is intended as a demo to send the input from user into the poe api, 
not for merchantability or any other commercial use """

import poe
Token = "TOKEN-HERE"
client = poe.Client(Token)

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
        input_language = "its original language"
    prompt = f"""
    your task is to translate the text delimited by triple backticks from {input_language} to {output_language}:
    only return the final translated text without quotation marks or backticks or any other delimiters or other preamble or postscript
    ```{input_text}```
    """
    response = get_response(prompt)
    return response



