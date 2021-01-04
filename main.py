from netcontroller import NetController
from flask import Flask
from flask_mail import Mail, Message
import pickledb
import json

def render_temp(argss,filename):
    htmlfile = open('templates/'+filename,'r').read()
    for me in argss:
        htmlfile = htmlfile.replace('%'+me+'%',argss[me])
    return htmlfile

db = pickledb.load('log.db', False)
net = NetController()
net.load_config('config.json')

app = Flask(__name__)
app.debug = True

try:
    conf = open('email.json').read()
    pass
except Exception as e:
    print('Can not open config file: '+str(e))
    conf = ''
    pass

if conf != '':
    jsconf = json.loads(conf)
    app.config['MAIL_SERVER'] = jsconf["smtp"]
    app.config['MAIL_PORT'] = int(jsconf["port"])
    if jsconf["tls"] == 'true':
        app.config['MAIL_USE_TLS'] = True
    else:
        app.config["MAIL_USE_TLS"] = False
    app.config['MAIL_USERNAME'] = jsconf["mail"]
    app.config['MAIL_DEFAULT_SENDER'] = jsconf["mail"]
    app.config['MAIL_PASSWORD'] = jsconf["pass"]
else:
    jsconf = {}
    jsconf["smtp"] = str(input('Enter your smtp server host or address: '))
    jsconf["port"] = str(input('Enter your smtp port: '))
    jsconf["tls"] = str(input('Use tls [true/false]: '))
    jsconf["mail"] = str(input('Enter your email: '))
    jsconf["pass"] = str(input('Enter your pass: '))
    f = open('email.json','w')
    f.write(str(jsconf).replace("'",'"'))
    f.close()
    app.config['MAIL_SERVER'] = jsconf["smtp"]
    app.config['MAIL_PORT'] = int(jsconf["port"])
    if jsconf["tls"] == 'true':
        app.config['MAIL_USE_TLS'] = True
    else:
        app.config["MAIL_USE_TLS"] = False
    app.config['MAIL_USERNAME'] = jsconf["mail"]
    app.config['MAIL_DEFAULT_SENDER'] = jsconf["mail"]
    app.config['MAIL_PASSWORD'] = jsconf["pass"]

mail = Mail(app)

@app.route('/')
def welcome():
    return 'Hello'

@app.route('/openported')
def port_opened():
    msg = Message("Feedback", recipients=[app.config['MAIL_USERNAME']])
    msg.body = "New port was opened on your server."
    try:
        mail.send(msg)
        return 'Success'
        pass
    except:
        pass
        return 'Not Success'
@app.route('/get_ports')
def portget():
    return net.get_ports('Hello')

app.run(host='0.0.0.0',port=1028)