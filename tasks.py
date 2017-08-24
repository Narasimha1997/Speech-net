import smtplib
from email.mime.text import MIMEText
from gtts import gTTS
import os

def send_mail(id,link):
    msg=MIMEText("You job is done, tap on this link to continue: "+link)
    msg['Subject']='Task complete'
    msg['From']='prasannahn1997@gmail.com'
    msg['To']=id
    server=smtplib.SMTP(host='smpt.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(user='prasannahn1997@gmail.com', password='Narasimha1997')
    server.sendmail(from_addr='prasannahn1997@gmail.com', to_addrs=id, msg=msg)
    server.quit()

def multimode_tts(text, f_name,lang,slow):
    if not os.path.exists('files'):
        os.mkdir('files')
    speech=gTTS(text=text,slow =slow, lang=lang)
    speech.save('files/'+f_name)

def task(id,gtts_text,lan,slow):
    bool_=False
    if slow=='slow':
        bool_=True
    multimode_tts(text=gtts_text, f_name='text.mp3', lang=lan, slow=bool_)
    send_mail(id=id, link='http://speech-net.herokuapp.com/job_cache')
    pass

def async_taskStart(parms):
    task(id=parms['id'], gtts_text=parms['text'], lan=parms['lang'], slow=parms['slow'])
