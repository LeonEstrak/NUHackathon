from flask import Flask, request
from flask_cors import CORS
from PIL import Image
import base64
from io import BytesIO, StringIO
import re
import os
#Waitress NGINX Flask
app = Flask(
    __name__,
    static_folder=os.getcwd() + '/build',
    static_url_path='/')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        image_data = re.sub('^data:image/.+;base64,', '',
                            data)
        # print(image_data)
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        SAVE_PATH = "image.png"
        IMG_FORMAT = "PNG"
        image.save(SAVE_PATH, IMG_FORMAT)
        return {"status": False}