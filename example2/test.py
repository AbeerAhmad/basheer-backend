import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)  # Need this because Flask sets up some paths behind the scenes
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise'] # this is what we will see in html page

@app.route("/") # by this index function will converted into flask function
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        #import tensorflow as tf
        # import numpy as np
        # from keras.preprocessing import image
        #
        # from keras.models import load_model
        # new_model = load_model('cat_dog_classifier.h5')
        # new_model.summary()
        # test_image = image.load_img('images\\'+filename,target_size=(128,128))
        # test_image = image.img_to_array(test_image)
        # test_image = np.expand_dims(test_image, axis = 0)
        # result = new_model.predict(test_image)
        import numpy as np
        from tensorflow.keras.preprocessing import image

        from tensorflow.keras.models import load_model
        model = create_model()
        model = model.load_weights('/Users/riley/Documents/Python Documents/ArtificialIntelligence/SemesterProject/emotionCNN.h5')
        # new_model.summary()
        img = np.array(img)
        img = np.expand_dims(img,axis = 0) #makes image shape (1,48,48)
        img = img.reshape(1,48,48,1)
        result = model.predict(img)
        result = list(result[0])
        label_dict = {0:'Angry',1:'Disgust',2:'Fear',3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}
        img_index = result.index(max(result))
        prediction =label_dict[img_index]
        plt.show()
        
        
        # result1 = result[0]
        # for i in range(6):
        #
        #     if result1[i] == 1.:
        #         break;
        # prediction = classes[i]

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("template.html",image_name=filename, text=prediction)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True)

