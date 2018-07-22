import cv2 
from pathlib import Path
import os  
from imutils import paths
import matplotlib.pyplot as plt
preprocessed_folder = "image_preprocessed"
input_folder = ['virat_kohli', 'sachin']

if not os.path.exists(preprocessed_folder):
    os.makedirs(preprocessed_folder)

for j, folder in enumerate(input_folder):
      
        for i, image in enumerate(paths.list_images(folder)) :

            try:
                image_data = cv2.imread(image)
                reshaped_image_data = cv2.resize(image_data, (250, 250))
                if j==0:
                    file = "virat"
                
                else:
                    file = "sachin"
                    
                file_name =f"{file}-{i}.jpg"
                print(file_name)
                if image_data is not None:
                    cv2.imwrite(os.path.join(preprocessed_folder, file_name), reshaped_image_data)

            except:
                print(f"Skipped {i}")
                pass    