#import os library
import os
import json
import shutil

#import mapping file:
from classes import parts_mapper, damage_mapper
everything_mapper = {**damage_mapper, **parts_mapper}


car_parts_ann_path = "data/Car parts dataset/File1/ann"


out_dir = "data/Car parts dataset/File1/labels" #where txt labels will go

# wipe the old folder before starting (if it exists)
if os.path.exists(out_dir):
    print(f"Cleaning up old labels: {out_dir}")
    shutil.rmtree(out_dir)

os.makedirs(out_dir, exist_ok=True)


yolo_lines = []

if not os.path.exists(car_parts_ann_path):
    print("path is incorrect, Check your path")


for file_name in sorted(os.listdir(car_parts_ann_path)):

    full_path = os.path.join(car_parts_ann_path, file_name)


    if file_name.endswith('.json'):
        with open(full_path, 'r') as file:
            data = json.load(file)

            img_width = data["size"]["width"]
            img_height = data["size"]["height"]

            #start extracting the objects
            for each_object in data['objects']:
                
                #get the id (for later remapping !!)
                class_name = each_object["classTitle"]
                if class_name in everything_mapper:
                    yolo_class_id = everything_mapper[class_name]
                else:
                    print(f"class name '{class_name}' not found in mapper!")
                    continue

                #The class id (maybe useful later)
                class_id = each_object['classId']
                
                #make a list specifically for this object
                current_object_points = [str(yolo_class_id)] #Put the class id in the beggining (as a string !!!) becuase yolo wants it to be string

                #start normalizing:
                for coordinates in each_object["points"]["exterior"]:

                    #Normalization for both (x,y)
                    x_norm = round(coordinates[0] / img_width , 8)
                    y_norm = round(coordinates[1] / img_height , 8)

                    current_object_points.append(str(x_norm))
                    current_object_points.append(str(y_norm))

                    #convert them from ['1', '0.5', '0.6'] to ----> '1' '0.5' '0.6' 
                
                    single_yolo_lines = " ".join(current_object_points)
                #end of Normalization loop
                
                yolo_lines.append(single_yolo_lines)
            #end of each_object loop

        #get the same name but change it from json to txt
        txt_filename = file_name.replace('.json' , ".txt")

        #now get the full path:
        txt_path = os.path.join(out_dir , txt_filename)

        #make the txt files now !!
        with open(txt_path , "w") as file:
            for line in yolo_lines:
                file.write(line + "\n")

        #صفّر العداد عشان اللي بعده يجي في سطر جديد
        yolo_lines = []
        
    #end of (json files)   

