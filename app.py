from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@socketio.on('test')
def handle_test(json):
    print('received json: ' + str(json))
    socketio.emit('play', {'msg': 'Go play!'})

if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8000, debug=True)
    socketio.run(app, host="0.0.0.0", port=5000, debug=1)
