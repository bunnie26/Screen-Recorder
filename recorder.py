from PIL import ImageGrab
import numpy as np
import cv2 
import datetime
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'


fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
captured = cv2.VideoWriter(file_name ,fourcc ,10.0 ,(w,h))


while True:
    Img = ImageGrab.grab(bbox=(0,0,w,h))
    Img_arr = np.array(Img)
    Img_final = cv2.cvtColor(Img_arr,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen recorder',Img_final)
    captured.write(Img_final)
    if cv2.waitKey(10) == ord('q'):
        break

