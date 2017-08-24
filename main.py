from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
import tasks
from threading import Thread
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

@app.route('/long_upload',methods=['POST'])
def long_upload():
    parms={'id':request.form['id'], 'text':request.form['text'], 'lan':request.form['lan'], 'slow':request.form['slow']}
    Thread(target=tasks.async_taskStart, args=(parms,)).start()
    return render_template('message.html')

@app.route('/job_cache', methods=['GET'])
def render_file():
    return send_from_directory(directory='files', filename='text.mp3')
