# Distance-Based Classification Lab-5 MLPR

## Overview
This lab implements face detection and clustering using distance-based classification methods. The implementation uses OpenCV's haar cascade classifier for face detection and K-means clustering

Image logging metrics detected on w&b
![image](https://github.com/user-attachments/assets/24cc12ce-8ccd-4db2-91ac-4665faab2dd4)

Showing Plotted Images on w&b
![image](https://github.com/user-attachments/assets/feb29336-2e75-4cd7-99dd-272d7dbc5658)

Showing Table on w&b
![image](https://github.com/user-attachments/assets/18b5c3bb-c619-489e-a107-e78de70e70ce)

Clustering Example
![image](https://github.com/user-attachments/assets/2762c71f-2d8a-4cd9-9c53-ba811ad08b62)

For Sashi Tharoor
<img width="429" alt="Screenshot 2025-02-26 at 3 13 52 AM" src="https://github.com/user-attachments/assets/f4d5e348-3181-49f6-8572-ffa491d2d926" />


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
