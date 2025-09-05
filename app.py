
import os
import time
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

# ---- Config ----
MODEL_PATH = os.environ.get("MODEL_PATH", "weights/best.pt")
YOLOV5_DIR = os.environ.get("YOLOV5_DIR", "yolov5")
UPLOAD_DIR = "uploads"
OUTPUT_DIR = os.path.join("static", "out")
ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

# ---- Load model ----
import torch  # torch will be provided by Dockerfile / requirements
if os.path.isdir(YOLOV5_DIR):
    # load from local repo to avoid internet at runtime
    model = torch.hub.load(YOLOV5_DIR, "custom", path=MODEL_PATH, source="local")
else:
    # fall back to GitHub (requires internet)
    model = torch.hub.load("ultralytics/yolov5", "custom", path=MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if not file or file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ALLOWED_EXT:
            flash(f"Unsupported file type: {ext}")
            return redirect(request.url)

        # unique filename to avoid collisions
        filename = secure_filename(f"{int(time.time())}_{file.filename}")
        in_path = os.path.join(UPLOAD_DIR, filename)
        file.save(in_path)

        # inference
        results = model(in_path, size=640)
        out_file = os.path.join(OUTPUT_DIR, os.path.basename(in_path))
        results.render()  # render predictions in memory
        from PIL import Image
        Image.fromarray(results.ims[0]).save(out_file)


        return redirect(url_for("result", in_name=filename, out_name=filename))
    else:
        return render_template("index.html")
@app.route("/result")
def result():
    in_name = request.args.get("in_name")
    out_name = request.args.get("out_name")
    if not in_name or not out_name:
        return redirect(url_for("index"))
    return render_template("result.html",
                           input_url=url_for("uploaded_file", filename=in_name),
                           output_url=url_for("static", filename=f"out/{out_name}"))

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
