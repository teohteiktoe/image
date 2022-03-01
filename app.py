#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image #use PIL
import numpy as np

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = "static/"


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save("static/" + filename)
        file = open("static/" + filename,"r")
        model = load_model("Flower")
        img = Image.open(filename) #rose = 3, sunflower = 4, tulip 5
        img = img.resize((100,100))
        img = np.asarray(img, dtype="float32") #need to transfer to np to reshape
        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3
        img.shape
        pred=model.predict(img)
        return(render_template("index1.html", result=str(pred)))
    else:
        return(render_template("index1.html", result="2"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




