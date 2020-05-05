#Developed by Mohammad Rahimzadeh
#https://github.com/mr7495
#By using this code, you can extract the frames of the videos
# You have to select the video path and the path to where frames are saved.
#You can choose the size of the generated frames.

import cv2
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--video_path", help="The path to the video")
parser.add_argument("--save_folder", help="The path to write the frames")
parser.add_argument("--height", default=1070, help="The height of the generated frames")
parser.add_argument("--width", default=600, help="The width of the generated frames")

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
  

args = vars(parser.parse_args())
if args["save_folder"] is  None:
    raise ValueError('The save_folder is empty')
elif args["video_path"] is  None:
    raise ValueError('The video_path is empty')
try:
    int(args["height"])
except:
    raise ValueError('height is not valid')
try:
    int(args["width"])
except:
    raise ValueError('width is not valid')
else:
    frame_generator(args["video_path"],args["save_folder"],size=(int(args["height"]),int(args["width"])))
        
        