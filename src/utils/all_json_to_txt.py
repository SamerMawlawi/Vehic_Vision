import os        #to handel paths and folders
import json      #to handel JSON
import shutil    #for directory removing
from classes import parts_mapper,damage_mapper #classes for remapping (taken from classes.py)

everything_mapper = {**damage_mapper, **parts_mapper} #combine both dicitonaries into 1

#make a function that takes (ann_dir , label_dir , mapper)
def convert_json_to_txt(ann_dir, label_dir, mapper):

    #if there are already label folder (clean it):
    if os.path.exists(label_dir):
        print(f'Cleaning up: {label_dir}')
        shutil.rmtree(label_dir)

    os.makedirs(label_dir, exist_ok=True)

    if not os.path.exists(ann_dir):
        print(f"Error, {ann_dir} Not found")

    processed = 0 #store the number of processed files.


    # Start the main loop
    for file_name in sorted(os.listdir(ann_dir)):
        
        full_path = os.path.join(ann_dir, file_name)
        
        if file_name.endswith('.json'):
            with open(full_path, 'r') as file:
                data = json.load(file)
                img_width = data["size"]["width"]
                img_height = data["size"]["height"]

                # Important: Reset yolo_lines for EVERY new file
                yolo_lines = []

                for each_object in data['objects']:
                    #get the class Title and find it in mapper
                    class_name = each_object["classTitle"]
                    class_id = each_object['classId'] #maybe useful later
                    
                    if class_name in mapper:
                        yolo_class_id = mapper[class_name]
                    else:
                        print(f" Warning: class name '{class_name}' not found in mapper!")
                        continue # Skip unknown classes

                    # Start object list with the mapped ID
                    current_object_points = [str(yolo_class_id)] 

                    for coordinates in each_object["points"]["exterior"]:
                        # Normalization for both (x,y)
                        x_norm = round(coordinates[0] / img_width, 8)
                        y_norm = round(coordinates[1] / img_height, 8)

                        current_object_points.append(str(x_norm))
                        current_object_points.append(str(y_norm))
                    
                    # Convert list to space-separated string
                    yolo_lines.append(" ".join(current_object_points))

            # Save to .txt file after finishing all objects in the image
            txt_filename = file_name.replace('.json', '.txt')
            txt_path = os.path.join(label_dir, txt_filename)

            with open(txt_path, "w") as f:
                for line in yolo_lines:
                    f.write(line + "\n") # Write each object on a new line
            
            processed += 1

    print(f"DONE: Processed {processed} files in {label_dir}")
    return


# --- Launching the function ---

if __name__ == "__main__":
    # Damage Dataset
    convert_json_to_txt(
        ann_dir="data/Car damages dataset/File1/ann",
        label_dir="data/Car damages dataset/File1/labels",
        mapper=everything_mapper
    )

    # Parts Dataset
    convert_json_to_txt(
        ann_dir="data/Car parts dataset/File1/ann",
        label_dir="data/Car parts dataset/File1/labels",
        mapper=everything_mapper
    )
