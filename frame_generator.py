import cv2
import os
def frame_generator(video_path,save_folder,size=(1070,600)):
    try:
        os.mkdir(save_folder)
    except:
        pass
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        ret,frame = cap.read()
        if ret is True:
            image=cv2.resize(frame,size)
            cv2.imwrite("{}/{}.jpg".format(save_folder,count), image)
            count = count + 1
        else:
            break
    cap.release()