# Transfer Learning with Google's Xception
A plant seedling classifier using transfer learning technique on Google's Xception model

&nbsp;

## Dataset
The Aarhus University Signal Processing group, in collaboration with University of Southern Denmark, released a dataset containing images of approximately 960 unique plants belonging to 12 species at several growth stages.
###### CATEGORIES
      ['Loose Silky-bent',
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
  
Kaggle has the complete dataset used for a competition here:  

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp; https://www.kaggle.com/c/plant-seedlings-classification/data  

&nbsp;

## Project reference
This project was created as a learning experience after 2 years of competition on tensorflow.
It achieved an accuracy of 94.2% in the competition, here is a link to the notebook:  

&nbsp;
  
&nbsp;&nbsp;&nbsp;&nbsp; https://www.kaggle.com/niteshksingh/transfer-learning-xception-96  
   
&nbsp;
  
## Saved Model (including weights)
A saved Model that can be easily used with tensorflow has been included in the "Model" directory.  
&nbsp;&nbsp;&nbsp;&nbsp; example: model = tf.keras.models.load_model("saved_model")

&nbsp;

## Check the model out
I am also including a py script you can directly use to classify images as "run.py".  
Use this syntax in the project directory: 
&nbsp;&nbsp; ***python3 run.py \<True path to image1\> \<True path to image2\> \<True path to image3\> ...***  
Note: You will need cv2 and tensorflow 2+ installed in a python environment to run the script.

&nbsp;
&nbsp;
&nbsp;
&nbsp;

Thank you for your time.
