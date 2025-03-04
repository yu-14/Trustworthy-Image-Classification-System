import tensorflow as tf
from PIL import Image
import numpy as np

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# Save some training images
for i in range(10):
    img = train_images[i]
    img = img.astype('uint8')  # Convert to uint8
    im = Image.fromarray(img, mode='L')  # 'L' for grayscale
    im.save(f'train_image_{i}.png')