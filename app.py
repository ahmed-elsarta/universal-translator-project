from flask import Flask, render_template, request, url_for
import translation
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods = ['POST'])
def translate():
    input_lang = request.form.get('input_lang')
    output_lang = request.form.get('output_lang')
    input_text = request.form.get('input_text')
    # translate the input
    output_text = translation.translate(input_lang, output_lang, input_text)
    # status_message = f"source language {input_lang} and target language {output_lang}, input text {input_text}"
    return output_text
if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True)