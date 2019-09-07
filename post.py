from flask import Flask, request, redirect, url_for, abort,  json
import messenger

app = Flask(__name__)

subscribed = False

@app.route('/')
def home():
    html = "<html>" \
           "<head><title>Welcome to Flask</title></head>" \
           "<body><h3>Welcome to Flask</h3>" \
           "<p>to subscribe go to /subscribe</p>" \
           "<p>to subscribe go to /publish</p>" \
           "<p>to subscribe go to /allMessages</p></body></html>"
    return html


@app.route('/subscribe')
def subscribe():
    global subscribed
    if subscribed == False:
        messenger.subscribe_on_topic()
    subscribed = True
    html = "<b>Subscribed</b>"
    return html.format()

@app.route('/allMessages')
def showAllMessages():
    list_lines = str(messenger.read_message()).split('\n')
    html = ''
    for line in list_lines:
        html += "<p>" + str(line)+"</p>"
    return html.format()

@app.route('/publish')
def send_messages():
    messenger.publish_on_topic()
    html = "<b>Message published</b>"
    return html.format()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)