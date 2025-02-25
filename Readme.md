# Distance-Based Classification Lab-5 MLPR

## Overview
This lab implements face detection and clustering using distance-based classification methods. The implementation uses OpenCV's haar cascade classifier for face detection and K-means clustering

## Uses
- Face detection using Haar Cascade Classifier
- K-means clustering (k=2) for face classification
- Feature extraction using hue and saturation values
- Wandb integration for experiment tracking

## Results
The implementation achieved:
- Successfully detected faces in group photos
- Clustered faces into 2 groups based on color features
- Tracked metrics using Weights & Biases:
  - Number of faces detected
  - Cluster sizes
  - Distribution of faces across clusters

## Key Findings
1. **Distance Metrics**: Explored various distance metrics.
2. **Applications**: Demonstrated real-world applications of distance metrics -- Face Recognition.

## Usage
1. `pip install -r requirements.txt`
2. Create `.env` and add your wandb api key
3. Run the Jupyter notebook
4. View results in Weights & Biases dashboard
