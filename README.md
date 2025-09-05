
# YOLO Object Detection — Flask + Docker

Minimal web app to serve a YOLOv5 model with Flask. Upload an image, get predictions drawn on the image.

## 1) Place your model
Put your trained weights at: `weights/best.pt`

## 2) Run with Docker (recommended)

```bash
docker build -t yolo-app .
docker run -p 5000:5000 yolo-app
# Open http://localhost:5000
```

The Docker image clones the YOLOv5 repo and installs its requirements (PyTorch, OpenCV, etc.).
No internet is required at runtime.

## 3) Local (without Docker)
> Requires Python 3.10+

```bash
pip install -r requirements.txt
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt
export MODEL_PATH=weights/best.pt
export YOLOV5_DIR=yolov5
python app.py
```

Then open `http://127.0.0.1:5000`

## 4) Deploy (two easy options)

### Option A — Hugging Face Spaces (Docker)
- Create a new Space → SDK: **Docker**
- Upload all files (including `weights/best.pt` into `weights/`)
- The build uses the provided `Dockerfile`

### Option B — Render (Docker)
- Push this folder to a GitHub repo
- Create a **Web Service** from the repo (Docker)
- Free instance is fine. Ensure `weights/best.pt` exists in the repo (or download it during build).

⚠️ If your weights are large, consider Git LFS or uploading them directly to the host (Spaces lets you upload via UI).

## 5) Deliverables (per challenge)
- **Model File(s):** `weights/best.pt` (and any tokenizer/config if needed)
- **Flask App Files:** `app.py`, `templates/`, `static/`, any utils
- **Dockerization:** `requirements.txt`, `Dockerfile`
- **Deployment Link:** public URL (Render / HF Spaces / Railway / Fly.io)
- **Slides Link:** add your link inside `slides_link.txt`

## 6) Notes
- `app.py` loads YOLO from local `yolov5` repo inside Docker to avoid runtime internet.
- If you need a different model path, set `MODEL_PATH` env var.
- For JSON API instead of HTML, add an `/api/predict` route and return boxes/scores.

---
**Extra Mile:** Polish your GitHub README with a GIF/screenshot and clear setup steps.
