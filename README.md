# Kohli_Sachin_Image-Classifier

Sachin <> Kohli  Image Classifier using CNN Network implemented using Keras library(TF Backend).

To run this on your computer :
 
 1) Download kohli/sachin images using this script or manually.
 
      <code> python image_scrapper.py </code>
     
     Also, download someother photos for training the NN other than kohli/sachin images for proper training.
 
 2) Preprocess the images to feed into the Network.
  
    For this network I, 
         a) Resized all the images to 250 x 250 x 3.
         b) Image -= Average(Image_pixels) / Standard_Deviation(Image_pixels)
         c) Image /= 255  (To make the input pixels lie in between 0 and 1) 
         
      <code> python image_preprocessing.py </code>

 3) Train the Network and save the model .
 
    <code> python model.py </code>
 
 4) Test the Network .
    
     <code> python model_test.py </code>
