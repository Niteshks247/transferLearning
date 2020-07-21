print("Importing Modules")
import sys
import tensorflow as tf
import cv2
import numpy as np

IMG_S1, IMG_S2 = (140,140)
CATEGORIES = ['Loose Silky-bent',
             'Common Chickweed',
             'Black-grass',
             'Charlock',
             'Small-flowered Cranesbill',
             'Sugar beet',
             'Maize',
             'Fat Hen',
             'Cleavers',
             'Common wheat',
             'Scentless Mayweed',
             'Shepherds Purse']

print("Importing Model")
model = tf.keras.models.load_model("saved_model")

print("Creating test set")
X = []
index = []
for i in range(1,len(sys.argv)):

    imgdir = sys.argv[i]
    image = cv2.imread(imgdir, cv2.IMREAD_ANYCOLOR)

    if image is None:
        print("Image not found, dir:",imgdir)
    else:
        image = cv2.resize(image , (IMG_S1, IMG_S2))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        X.append(image)
        index.append(i)
    
X = np.array(X)/255.
result = model.predict_classes(X)
print("-------------------------")
for i in range(len(index)):
    print(index[i]," : ",CATEGORIES[result[i]])
print("------------------------------")
print("End")