from flask import Flask, request, render_template
from Transliterate import Transliterate

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('Formoo.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['Textoo']
    lang = request.form['langoo']
    src = request.form['srcoo']
    # print(text, lang)
    return Transliterate(text, lang, src)+'''<br></br><input type=button value="Previous Page" onClick="javascript:history.go(-1);">'''


if __name__ == '__main__':
    app.run()
