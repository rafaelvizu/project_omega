from flask import Flask, Response
from dotenv import load_dotenv
import os
from helpers.HomeHelper import HomeController

load_dotenv()
app = Flask(__name__)

@app.route('/')
def video_feed():
    return Response(HomeController.generateFrames(RTSP_URL=os.getenv('RTSP_URL')), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)