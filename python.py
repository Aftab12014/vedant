from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    filename = video.filename
    video.save(os.path.join('uploads', filename))
    return 'Video uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)