import os
import gtts
from flask import Flask, render_template, request, redirect
#from langdetect import detect
from playsound import playsound

app = Flask(__name__)

@app.route("/")
def customer():
    return render_template('text.html')


@app.route('/success', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        text1 = str(request.form.getlist("name"))

        tts = gtts.gTTS(text1, lang="en")
        tts.save("D:/python/aids/my-translation1.mp3")
        playsound("D:/python/aids/my-translation1.mp3")
        #os.remove("my-translation1.mp3")
    return render_template("result_data.html", result=text1)


if __name__ == '__main__':
    app.run(debug=True)