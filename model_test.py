import cv2 
import numpy as np 
import keras 
import matplotlib.pyplot as plt 

model = keras.models.load_model('model.h5', compile= True)
 
image = cv2.imread('scf_test.jpg')
plt.imshow(image)

image = cv2.resize(image, (250, 250))
image = np.array(image)
image = np.reshape(image, (1, 250, 250 , 3))
image = image -np.average(image)/np.std(image)
image /= 255

# new_image = numpy.reshape(new_image, (-1, 250, 250, 3))
y1 = model.predict(image)
y=model.predict_classes(image)

print(y, np.argmax(y), y1)
plt.show()
