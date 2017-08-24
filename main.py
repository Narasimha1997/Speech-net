from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
app=Flask(__name__, static_url_path="/cache")

def sound_gen(text,lan,mode):
    tts=gTTS(text=text,slow =mode, lang = lan )
    tts.save("cache/text.mp3")

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/start',methods=['GET'])
def start():
    return render_template('main.html')

@app.route('/convert', methods=['POST'])
def convert():
    text=request.form['txt']
    lan=request.form['lan']
    res=False
    if request.form['mode']=='slow':
        res=True
    sound_gen(text=text,lan=lan,mode=res)
    return send_from_directory(as_attachment=True, directory='cache', filename='text.mp3')
