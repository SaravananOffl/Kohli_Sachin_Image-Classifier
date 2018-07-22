import os
from imutils import paths
import cv2
import requests
from pathlib import Path
import matplotlib.pyplot as plt

""" 
    make sure to parse through all the images
    in the website, and save it in a .txt file

    In JS Console run 
    var script = document.createElement('script');
    script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
    document.getElementsByTagName('head')[0].appendChild(script);
    var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
    var textToSave = urls.toArray().join('\n');
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
    hiddenElement.target = '_blank';
    hiddenElement.download = 'urls.txt';
    hiddenElement.click();

"""

file_name = "virat_kohli_url.txt"
output_folder = Path("virat_kohli")

urls = open(file_name).read().strip().split('\n')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
    
for i, url in enumerate(urls):
    try: 
        request = requests.get(url, timeout = 60)
        
        output_filename = f'viratkohli{i}.jpg'
        new_file = output_folder/output_filename
        
        file = open(new_file, "wb")
        file.write(request.content)
        file.close()
        print(f"downloaded {i}")
    except:
        print(f"Skipped {i}")
        