import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image
from ultralytics import YOLO
import shutil

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/uploads'

# Fungsi untuk merender halaman Home
@app.route("/")
def uploader():
    path = app.config['UPLOAD_PATH']
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(os.path.join(path, x)))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    return render_template("index.html", uploads=uploads)

# Fungsi untuk merender halaman About
@app.route("/about")
def about():
    return render_template("about.html")

# Fungsi untuk merender halaman Gallery
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# Fungsi untuk merender halaman Support
@app.route("/support")
def support():
    return render_template("support.html")

# Fungsi untuk merender halaman Upload
@app.route("/upload", methods=['POST'])
def upload_file():
    if 'file' in request.files:
        f = request.files['file']
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_PATH'], filename)
        f.save(filepath)

        # Perform YOLO detection
        yolo = YOLO('best.pt')

        # Load image using PIL
        image = Image.open(filepath)

        # Perform YOLO detection
        detections = yolo.predict(image, imgsz=640, conf=0.6, save=True, project="static/", name="uploads", exist_ok=True)
        print(detections)

        return redirect("/")

if __name__ == "__main__":
    app.run()