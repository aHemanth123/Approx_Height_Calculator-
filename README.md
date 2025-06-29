 # 📏 Real-Time Height Estimation using OpenCV & MediaPipe

This project performs real-time human height estimation using webcam video feed, leveraging **MediaPipe Pose Detection** and **OpenCV**. It tracks key landmarks such as the top of the head and the heels to estimate a person's height. It also compares the height of two individuals in the frame and labels the taller and shorter person.

---

## 🧠 Features

- 🎥 Real-time webcam capture using OpenCV.
- 🕴️ Pose detection using **MediaPipe**.
- 📐 Height estimation using distance between `LEFT_EAR` and `LEFT_HEEL`.
- 🔢 Converts height in inches to feet and inches format.
 
- 🖥️ Full-screen OpenCV window.
- 👁️ Flip view for natural mirror effect.


 

## ⚙️ How It Works

1. **Pose Detection:**
   - Uses MediaPipe to detect body landmarks.
   - Focuses on vertical pixel distance from head to heel.

2. **Height Calculation:**
   - Height (in pixels) is converted to inches using:
     ```
     height_inches = pixel_height / 6.5
     ```
     This is an estimated scale factor. For better accuracy, calibrate using an object of known height.

3. **Conversion:**
   - Inches are converted to `ft` + `in` format for better readability.

 

###  Enhancements 

4. **Comparison:**
   - If two people are detected, their estimated heights are compared.
   - Labels are drawn for "Taller" and "Shorter".


 
## 🧪 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/height-estimation.git
cd height-estimation

```

## 2 Install Dependencies
Create requirements.txt with:
```
opencv-python
mediapipe
numpy
```
```
pip install -r requirements.txt
```


## Run the Project
```
python main.py
```
### Instructions 

Ensure your webcam is connected and functioning. 
The application will run in full screen.    
Press Q to quit.  

###  Concepts  
📌 Pose Estimation    

MediaPipe provides 33 body landmarks.
We use LEFT_EAR for the head and LEFT_HEEL for the foot.

🧮 Height Scaling   
Approximation assumes 1 inch ≈ 6.5 pixels (adjustable).
Can be calibrated using a reference object like an A4 sheet or ruler.

✅ Real-time Feedback   
Displays estimated height above head.
Compares two users to label taller/shorter persons.


### Enchancements 
- 🤝 Compares multiple people in the frame and shows:
  - ✅ "Taller"
  - ✅ "Shorter"
    
To Use Need to Use Yolo Method 
