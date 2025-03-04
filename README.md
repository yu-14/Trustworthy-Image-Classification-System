# Trustworthy Image Classification System
A system using blockchain for image integrity and machine learning for classification.

## Features
- Stores image hashes on a custom blockchain to detect tampering.
- Uses a CNN trained on Fashion-MNIST (90% accuracy) to classify clothing items.
- Demonstrates tampering detection by rejecting modified images.

## Files
- `blockchain.py`: Custom blockchain implementation.
- `image_hash.py`: SHA-256 hashing for images.
- `model.py`: CNN training and classification.
- `main.py`: Menu-driven interface.
- `save_images.py`: Saves Fashion-MNIST images for testing.

## Usage
1. Run `python main.py`.
2. Add images to the trusted list (option 1).
3. Classify images (option 2), rejecting tampered ones.

## Requirements
- Python 3.8+, TensorFlow, PIL
