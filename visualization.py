#Developed by Mohammad Rahimzadeh
#https://github.com/mr7495
#Use this code to plot the annotation on the images.

import csv
import cv2
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--annotation_path", help="The path to the annotation CSV file")
parser.add_argument("--images_path", help="Path to the dataset images")
parser.add_argument("--save_path", help="Path to write the plotted images")

def plot_boxes(annotation_path,images_path,save_path):
    try:
        os.mkdir(save_path)
    except:
        pass
    anno=[]
    names=[]
    with open(annotation_path,newline='', mode='r') as csvfile:
         csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         for row in csv_reader:
             anno.append(row)
             if row[0] not in names:
                 names.append(row[0])
    for name in names:
        data=[]
        for row in anno:
            if row[0]==name:
                data.append(row)
                
        image=cv2.imread('{}/{}'.format(images_path,name))
        for d in data:
            b=np.array(d[1:5]).astype(int)
            if d[5]=='0':
                color=(0,0,255)
            if d[5]=='1':
                color=(255,0,0)
            cv2.rectangle(image, (b[0], b[1]), (b[2], b[3]),color, thickness=5)
        cv2.imwrite('{}/{}'.format(save_path,d[0]),image)
    
args = vars(parser.parse_args())
if args["annotation_path"] is  None:
    raise ValueError('The annotation_path is empty')
elif args["images_path"] is  None:
    raise ValueError('The images_path is empty')
elif args["save_path"] is  None:
    raise ValueError('The save_path is empty')
else:
    plot_boxes(args["annotation_path"],args["images_path"],args["save_path"])