#Developed by Mohammad Rahimzadeh
#https://github.com/mr7495

#This program helps you label the objects in the images
#In this case, we have only two classes, so run the program and set the box around the object, then press enter
# after that, press 0 or 1. 0 is referred to class 1, and 1 is referred to class2. 
#If you press any other keys after pressing enter, the selected box would be rejected.
#If you want to go to the next image, select a random box, press enter, then press n.
#If you want to quit, select a random box, press enter, then press e.
#The labels of each image would be saved to the inserted save_path in a CSV file.


import os
import cv2
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--images_path", help="The path to the images")
parser.add_argument("--save_path", help="The path to save the annotation csv files")



def write_on_csv(image_name,image_data,csv_path):
    
    with open('{}/Data {}.csv'.format(csv_path,image_name), mode='w',newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        for data in image_data:
            write_data=[image_name]
            write_data.extend([data[1][0],data[1][1],data[1][0]+data[1][2],data[1][1]+data[1][3],data[0]])
            csvwriter.writerow(write_data)  
            print(write_data)
        csv_file.close()
        
        
def make_label(imgs_path,csv_path):
    if not os.path.exists(csv_path):
        os.mkdir(csv_path)
        
    files=[]
    images_names=[]
    for r,d,f in os.walk(imgs_path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r,file))
                images_names.append(file)
    
    images_path=files.copy()  
    
    done=False
    for image_index,image_path in enumerate(images_path):
        if done==True:
            break
        image_data=[]       
        image = cv2.imread(image_path)
        while(True):
            r = cv2.selectROI(image)
            key = cv2.waitKey(0) & 0xFF
            if key == ord("0"):
                image_data.append([0,r])
            elif key == ord("1"):
                image_data.append([1,r])
            elif key == ord("n"):
                write_on_csv(images_names[image_index],image_data,csv_path) 
                break
            elif key == ord("e"):
                write_on_csv(images_names[image_index],image_data,csv_path)
                done=True
                break
    
    cv2.destroyAllWindows()
    
args = vars(parser.parse_args())
if args["images_path"] is  None:
    raise ValueError('The images_path is empty')
elif args["save_path"] is  None:
    raise ValueError('The save_path is empty')
else:
    make_label(args["images_path"],args["save_path"])
        
        