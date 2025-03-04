import hashlib

def compute_image_hash(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return hashlib.sha256(image_data).hexdigest()