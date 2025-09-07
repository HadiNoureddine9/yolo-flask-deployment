# YOLO Object Detection Flask App 🚀

A modern, containerized web application for real-time object detection using YOLOv5 and Flask. Upload images and get instant object detection results with bounding boxes and confidence scores.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-FF6B35?style=for-the-badge&logo=ultralytics&logoColor=white)

## ✨ Features

- 🖼️ **Image Upload**: Support for multiple image formats (JPG, PNG, BMP, GIF, WEBP)
- 🔍 **Real-time Detection**: Instant object detection with YOLOv5
- 🎯 **Bounding Boxes**: Visual detection results with confidence scores
- 🐳 **Docker Ready**: Complete containerization with optimized Docker setup
- 🚀 **Production Ready**: Gunicorn WSGI server for production deployment
- 📱 **Responsive UI**: Clean, modern web interface
- ⚡ **Fast Inference**: Optimized for quick processing
- 🔧 **Configurable**: Environment-based configuration for different deployments

## 🏗️ Architecture

```
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── templates/            # HTML templates
│   ├── index.html        # Upload interface
│   └── result.html       # Results display
├── static/               # Static assets
├── uploads/              # Uploaded images (ignored)
├── yolov5/               # YOLOv5 repository
└── weights/              # Model weights
    └── best.pt           # Your trained model
```

## 🚀 Quick Start

### Using Docker 

```bash
# Clone the repository
git clone https://github.com/HadiNoureddine9/yolo-flask-deployment.git
cd yolo-flask-deployment

# Place your trained model weights
cp your-model.pt weights/best.pt

# Build and run with Docker
docker build -t yolo-detection .
docker run -p 5000:5000 yolo-detection
```

Open [http://localhost:5000](http://localhost:5000) in your browser!

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Clone YOLOv5
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt

# Set environment variables
export MODEL_PATH=weights/best.pt
export YOLOV5_DIR=yolov5

# Run the application
python app.py
```

## 🔧 Configuration

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `MODEL_PATH` | `weights/best.pt` | Path to YOLOv5 model weights |
| `YOLOV5_DIR` | `yolov5` | Path to YOLOv5 repository |
| `PORT` | `5000` | Server port |
| `SECRET_KEY` | `dev-secret-change-me` | Flask secret key |

## 📡 API Endpoints

### Web Interface
- `GET /` - Upload form
- `POST /` - Process uploaded image
- `GET /result` - Display detection results

### Static Files
- `/uploads/<filename>` - Access uploaded images
- `/static/<path>` - Access static assets


### Production Deployment

The app includes Gunicorn for production serving:

```dockerfile
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:5000", "app:app"]
```

## 🌐 Cloud Deployment

### Hugging Face Spaces Link:
https://huggingface.co/spaces/hno123/yolo-flask-deployment


## 📋 Requirements

- **Python**: 3.10 or higher
- **Docker**: For containerized deployment
- **Model**: YOLOv5 compatible weights file
- **Storage**: ~500MB for YOLOv5 dependencies

## 🔍 Model Configuration

 trained YOLOv5 model at:
```
weights/best.pt
```

The app automatically detects and loads the model on startup. For custom model paths, set the `MODEL_PATH` environment variable.

## 🎨 UI Features

- **Clean Interface**: Minimalist design with modern CSS
- **File Validation**: Client-side format checking
- **Responsive Design**: Works on desktop and mobile
- **Real-time Feedback**: Upload progress and error handling

## 🛠️ Development

### Project Structure
```
yolo-flask-deploy/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── templates/         # Jinja2 templates
├── static/            # CSS, JS, images
├── weights/           # Model weights directory
├── uploads/           # Temporary upload storage
└── yolov5/            # YOLOv5 framework
```

## 🚨 Troubleshooting

### Common Issues

1. **Model not found**: Ensure `weights/best.pt` exists
2. **Port already in use**: Change port with `-p 8080:5000`
3. **Memory issues**: Reduce image size or use smaller model
4. **GPU not detected**: Install CUDA drivers for GPU support

### Debug Mode

```bash
# Run with debug logging
docker run -e DEBUG=1 -p 5000:5000 yolo-app
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

- 📧 **Issues**: [GitHub Issues](https://github.com/HadiNoureddine9/yolo-flask-deployment/issues)
- 📖 **Documentation**: This README
- 🔧 **Updates**: Watch releases for new features

---

**Built with ❤️ using Flask, YOLOv5, and Docker**

*Star this repo if you find it helpful! ⭐*
