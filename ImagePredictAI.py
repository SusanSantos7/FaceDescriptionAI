import cv2  # Import OpenCV library
#from deepface import DeepFace

# Read input image
img = cv2.imread('image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eyes using a Haar cascade classifier
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

# Iterate through the eyes detected and draw a rectangle around them
for (x,y,w,h) in eyes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    
    # Get eye's color
    eye_img = img[y:y+h, x:x+w]
    eye_bgr = cv2.mean(eye_img)
    eye_color = 'unknown'
    
    # Assign eye color based on BGR values
    if eye_bgr[2] > eye_bgr[1] and eye_bgr[2] > eye_bgr[0]:
        eye_color = 'blue'
    elif eye_bgr[1] > eye_bgr[0] and eye_bgr[1] > eye_bgr[2]:
        eye_color = 'green'
    elif eye_bgr[0] > eye_bgr[1] and eye_bgr[0] > eye_bgr[2]:
        eye_color = 'brown'
    elif eye_bgr[2] > eye_bgr[0] and eye_bgr[2] > eye_bgr[1]:
        eye_color = 'gray'
    elif eye_bgr[1] > eye_bgr[2] and eye_bgr[1] > eye_bgr[0]:
        eye_color = 'hazel'
    elif eye_bgr[0] > eye_bgr[2] and eye_bgr[0] > eye_bgr[1]:
        eye_color = 'amber'
    else:
        eye_color = 'unknown'
    
    # Detect emotion 
    emotion_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    emotion = emotion_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in emotion:
        emotion_img = img[y:y+h, x:x+w]
        emotion_bgr = cv2.mean(emotion_img)
        emotion_color = 'unknown'
        
        # Assign emotion based on BGR values
        if emotion_bgr[2] > emotion_bgr[1] and emotion_bgr[2] > emotion_bgr[0]:
            emotion_color = 'happy'
        elif emotion_bgr[0] > emotion_bgr[1] and emotion_bgr[0] > emotion_bgr[2]:
            emotion_color = 'sad'
        elif emotion_bgr[1] > emotion_bgr[2] and emotion_bgr[1] > emotion_bgr[0]:
            emotion_color = 'angry'
        else:
            emotion_color = 'unknown'
            
        print('Eye color:', eye_color)
        print('Emotion:', emotion_color)
        break 
    break

# Show the image
cv2.imshow('Eye Detection', img)

# Wait until a key is pressed
cv2.waitKey(0)

# Release the image
cv2.destroyAllWindows()
