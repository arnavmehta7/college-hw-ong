import cv2

img = cv2.imread('./Plaksha_Faculty.jpg')
img2 = cv2.imread('./Dr_Shashi_Tharoor.jpg')

assert img is not None, "Image 1 is not loaded"
assert img2 is not None, "Image 2 is not loaded"

print("Images loaded successfully")

