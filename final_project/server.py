from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.english_to_french(textToTranslate)
    # Write your code here
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.french_to_english(textToTranslate)
    # Write your code here
    return englishText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html") # renders the index.html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
