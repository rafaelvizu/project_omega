from flask import Flask, Response
from dotenv import load_dotenv
import os
from helpers.FrameHelper import FrameHelper

load_dotenv()
app = Flask(__name__)
frameHelper = FrameHelper(os.getenv('PATH_TO_IMAGES'))

@app.route('/')
def video_feed():
    return Response(frameHelper.generateFrames(os.getenv('RTSP_URL')), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/update-storage', methods=['GET'])
def update_storage():
    frameHelper.update_storage()
    return 'Storage updated'


if __name__ == '__main__':
    app.run(debug=True)