from flask import Flask,render_template,request
import tensorflow as tf
from keras_preprocessing.image import img_to_array 
import matplotlib.pyplot as plt
import keras
from skimage.transform import resize
from keras import models
import numpy as np 



app = Flask(__name__)
model = keras.models.load_model('model.hdf5')


@app.route('/',methods =['GET'])

def hello_world():
    return render_template('index.html')

@app.route('/',methods =['POST'])
def predict():
    
    imagefile = request.files['imagefile']

    image_path = 'C:/Users/hanav/Desktop/nguyen_van_han/images/'+ imagefile.filename

    imagefile.save(image_path)

    #image = tf.keras.utils.load_img(image_path,target_size=(128,128))
    image = plt.imread(image_path)
    image = resize(image,(128,128))
    image = img_to_array(image)
    image = np.expand_dims(image,axis=0)
    predicted_result  = model.predict(image)

    if int(predicted_result*2)>=1:
        precentage = (round(float(((predicted_result[0]-0.5 ) +0.5 )* 100 ),3))
        label = f"Male:{precentage}%"
    else:
        precentage = (round(float(((0.5-predicted_result[0])+0.5)* 100 ),3))
        label = f"Female:{precentage}%"
    return render_template('index.html',prediction = label)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2500,debug=True)