from PIL import Image
import os
import numpy as np

#In fixed code below, had to assign result of img.resize back to img variable otherwise it was returning original images. 

# Define the directory where your downloaded images are located
downloaded_images_dir = 'C:\\Users\\Shivy\\Desktop\\Data_Sources\\Dataset_images\\I_test'
# Define the directory where you want to save resized images
resized_images_dir = 'C:\\Users\\Shivy\\Desktop\\Data_Sources\\Dataset_images\\test\\Influenzavirus'

# Ensure the output directory exists
os.makedirs(resized_images_dir, exist_ok=True)

# image size
target_size = (200, 200)

# Process each image in the downloaded directory
for filename in os.listdir(downloaded_images_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust based on image formats you have
        image_path = os.path.join(downloaded_images_dir, filename)
        
        # Open the image using PIL
        img = Image.open(image_path)
        
        # Resizes to 200x200, img.thumbnail was resizing while maintaining aspect ratio which was undesirable
        img = img.resize(target_size, Image.LANCZOS)  # Assign the resized image back to img
        
        # Convert image to RGB (in case it's grayscale) and ensure pixel range is 0-255
        img = img.convert('RGB')
        img_array = np.array(img)
        img_array = np.clip(img_array, 0, 255)  # Clip pixel values to 0-255
        img = Image.fromarray(np.uint8(img_array))
        
        # Save the resized image to the output directory
        save_path = os.path.join(resized_images_dir, filename)
        img.save(save_path)