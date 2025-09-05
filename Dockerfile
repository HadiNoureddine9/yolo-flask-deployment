
FROM python:3.10-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ffmpeg libsm6 libxext6 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Flask & server
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clone YOLOv5 and install its deps (includes torch, opencv, etc.)
RUN git clone https://github.com/ultralytics/yolov5.git
RUN pip install --no-cache-dir -r yolov5/requirements.txt

# App files
COPY . .

# Default model path (place your weights at weights/best.pt)
ENV MODEL_PATH=weights/best.pt
ENV YOLOV5_DIR=yolov5

RUN mkdir -p static/out uploads

EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:5000", "app:app"]
