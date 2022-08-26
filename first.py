import cv2
import tensorflow.keras
import numpy as np
from PIL import Image, ImageOps
# 카메라 캡쳐 객체, 0=내장 카메라
capture = cv2.VideoCapture(0)

# 캡쳐 프레임 사이즈 조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True: # 특정 키를 누를 때까지 무한 반복
    # 한 프레임씩 읽기
    ret, frame = capture.read()
    if ret == True: 
        print("read success!")
    
    # 이미지 뒤집기, 1=좌우 뒤집기
    frame_fliped = cv2.flip(frame, 1)
    
    # 읽어들인 프레임을 윈도우창에 출력
    cv2.imshow("VideoFrame", frame_fliped)
    
    # 1ms동안 사용자가 키를 누르기를 기다림
    if cv2.waitKey(1) > 0: 
        break 
        
# 카메라 객체 반환
capture.release()
cv2.destroyAllWindows()
 # Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('awake.jpg')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)


image.show()

normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)