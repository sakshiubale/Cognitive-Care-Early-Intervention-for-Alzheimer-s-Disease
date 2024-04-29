import numpy as np
import tensorflow as tf # type: ignore
import os
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array, load_img # type: ignore
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'



from flask import Flask , request, render_template # type: ignore
#from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

app = Flask(__name__,template_folder='templates')
model = load_model("model (1).h5" , compile = False)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/Doctors')
def doctors():
    return render_template('/Doctors.html')

@app.route('/pred.html')
def pred():
    return render_template('/pred.html')

def preprocess_image(img, target_size=(224, 224)):

   # Convert to NumPy array
   img = img_to_array(img)

   # Rescale (assuming your model expects normalized pixel values)
   img = img / 255.0  # Rescale to range [0, 1]

   # Resize if necessary
   if img.shape[0:2] != target_size:
     img = tf.image.resize(img, target_size)

   return img

@app.route('/pred',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        
        # Ensure the folder 'uploads' exists in the current directory
        uploads_dir = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        filepath = os.path.join(uploads_dir, f.filename)
        f.save(filepath)
       
        img = load_img(filepath, target_size=(299, 299))
        preprocessed_img = preprocess_image(img)

        x = preprocessed_img
        x = np.expand_dims(x, axis=0)
        preds = model.predict(x)
        
        index = ['MildDemented','VeryMildDemented','NonDemented','ModerateDemeneted']
        
        predicted_class_index = np.argmax(preds)
        predicted_class = index[predicted_class_index]
        
        text = "The predicted Alzhimer level is: " + predicted_class

        # Render predict.html with the prediction result
        return text

    # Render predict.html with empty text (if accessed via GET request)
    return render_template('templates/pred.html', text= "")
if __name__ == '__main__':
    app.run(debug = False, threaded = False)