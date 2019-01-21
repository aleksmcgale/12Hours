import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, redirect
from imageProcessing import visionAPI
from scripts import Filter_and_sort
import waste_wizard

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/svvarik/Documents/Projects/12Hours/uofthacksbeta19/PhotosToProcess'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

temp_list = []


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def landing_page():
    return render_template("index.html")


@app.route('/process_image', methods=["POST", "GET"])
def process_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            urLString = os.path.join(UPLOAD_FOLDER, filename)
            file.save(urLString)
            # Use Vision API to see what we have
            json = visionAPI.analyze_for_tags(urLString)
            tags = Filter_and_sort.json_to_tags(json)
            word = waste_wizard.get_json_data(tags[0])
            return render_template("index_2.html", container=word, object=tags[0])


        # return redirect(url_for('uploaded_file', filename=filename))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
