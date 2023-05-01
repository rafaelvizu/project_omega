from flask import Flask, Response
from dotenv import load_dotenv
import os
from controllers.FrameController import FrameController

load_dotenv()
app = Flask(__name__)
frameHelper = FrameController(os.getenv('PATH_TO_IMAGES'))

@app.route('/')
def video_feed():
    return Response(frameHelper.generateFrames(os.getenv('RTSP_URL')), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/update-storage', methods=['GET'])
def update_storage():
    FrameController.update_storage()
    return 'Storage updated'


if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=5000)