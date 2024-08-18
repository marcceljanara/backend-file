from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Path untuk menyimpan file yang diupload
UPLOAD_FOLDER_IMAGE = 'C:/Users/rogst/blockchain/iota-nft-python/dataset'
UPLOAD_FOLDER_MODEL = 'C:/Users/rogst/blockchain/iota-nft-python/dataset-models'

# Daftar ekstensi file yang diizinkan
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_H5_EXTENSIONS = {'h5'}

def allowed_file(filename, allowed_extensions):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Endpoint untuk menerima file gambar
@app.route('/upload/image', methods=['POST'])
def upload_file_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename, ALLOWED_IMAGE_EXTENSIONS):
        # Simpan file ke direktori yang ditentukan
        file_path = os.path.join(UPLOAD_FOLDER_IMAGE, file.filename)
        file.save(file_path)
        return jsonify({"message": "Image file uploaded successfully!"}), 200
    else:
        return jsonify({"error": "Invalid file type. Only image files are allowed."}), 400

# Endpoint untuk menerima file .h5
@app.route('/upload/h5', methods=['POST'])
def upload_file_h5():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename, ALLOWED_H5_EXTENSIONS):
        # Simpan file ke direktori yang ditentukan
        file_path = os.path.join(UPLOAD_FOLDER_MODEL, file.filename)
        file.save(file_path)
        return jsonify({"message": ".h5 file uploaded successfully!"}), 200
    else:
        return jsonify({"error": "Invalid file type. Only .h5 files are allowed."}), 400

if __name__ == '__main__':
    app.run(debug=True)
