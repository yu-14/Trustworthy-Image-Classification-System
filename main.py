from blockchain import Blockchain
from image_hash import compute_image_hash
from model import classify_image

blockchain = Blockchain()

def add_image_to_trusted_list(image_path):
    image_hash = compute_image_hash(image_path)
    blockchain.add_block(image_hash)
    print(f"Image {image_path} added to trusted list with hash {image_hash}")

def classify_image_if_trusted(image_path):
    image_hash = compute_image_hash(image_path)
    all_trusted_hashes = blockchain.get_all_hashes()
    if image_hash in all_trusted_hashes:
        classification = classify_image(image_path)
        print(f"The image is trusted and classified as {classification}")
    else:
        print("The image is not trusted or has been tampered with")

while True:
    print("1. Add image to trusted list")
    print("2. Classify image")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        image_path = input("Enter image path: ")
        add_image_to_trusted_list(image_path)
    elif choice == '2':
        image_path = input("Enter image path: ")
        classify_image_if_trusted(image_path)
    elif choice == '3':
        break
    else:
        print("Invalid choice")