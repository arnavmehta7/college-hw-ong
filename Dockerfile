FROM python:3.11
WORKDIR /app
RUN pip install numpy pandas scikit-learn wandb opencv-python
COPY . .
CMD ["python", "test_script.py"]