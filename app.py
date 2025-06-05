from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import numpy as np
import base64
import re
from PIL import Image
import io

app = Flask(__name__)
model = load_model("model_cnn.h5")

def preprocess_image(img_data):
    img_str = re.search(r'base64,(.*)', img_data).group(1)
    decoded = base64.b64decode(img_str)
    img = Image.open(io.BytesIO(decoded)).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img)
    img_array = 255 - img_array      # inversion (blanc sur noir)
    img_array = img_array / 255.0    # normalisation
    img_array = img_array.reshape(1, 28, 28, 1)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img_data = data['image']
    img_array = preprocess_image(img_data)
    prediction = model.predict(img_array).argmax()
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
