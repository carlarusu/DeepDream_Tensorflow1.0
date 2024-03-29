########################################################################
#
# Image manipulation utility functions
#
########################################################################

import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

########################################################################

# Function to load an image and return it as a numpy array of floating-points.

def load_image(filename):
    image = PIL.Image.open(filename)

    return np.float32(image)

########################################################################
	
# Function to save an image as a jpeg. The image is given as a numpy array with pixel-values between 0 and 255.

def save_image(image, filename):
    # Ensure the pixel-values are between 0 and 255.
    image = np.clip(image, 0.0, 255.0)
    
    # Convert to bytes.
    image = image.astype(np.uint8)
    
    # Write the image-file in jpeg-format.
    with open(filename, 'wb') as file:
        PIL.Image.fromarray(image).save(file, 'jpeg')
		
########################################################################

# Function to plot an image using PIL.

def plot_image(image):
    # Assume the pixel-values are scaled between 0 and 255.
    
    if False:
        # Convert the pixel-values to the range between 0.0 and 1.0
        image = np.clip(image/255.0, 0.0, 1.0)
        
        # Plot using matplotlib.
        plt.imshow(image, interpolation='lanczos')
        plt.show()
    else:
        # Ensure the pixel-values are between 0 and 255.
        image = np.clip(image, 0.0, 255.0)
        
        # Convert pixels to bytes.
        image = image.astype(np.uint8)

        # Convert to a PIL-image and display it.
        display(PIL.Image.fromarray(image))

########################################################################

# Function to normalize an image so its values are between 0.0 and 1.0. This is useful for plotting the gradient.

def normalize_image(x):
    # Get the min and max values for all pixels in the input.
    x_min = x.min()
    x_max = x.max()

    # Normalize so all values are between 0.0 and 1.0
    x_norm = (x - x_min) / (x_max - x_min)
    
    return x_norm

########################################################################

# Function to plot the gradient after normalizing it.

def plot_gradient(gradient):
    # Normalize the gradient so it is between 0.0 and 1.0
    gradient_normalized = normalize_image(gradient)
    
    # Plot the normalized gradient.
    plt.imshow(gradient_normalized, interpolation='bilinear')
    plt.show()

########################################################################

#This function resizes an image. It can take a size-argument where you give it the exact pixel-size you want the image to be e.g. (100, 200). Or it can take a factor-argument where you give it the rescaling-factor you want to use e.g. 0.5 for halving the size of the image in each dimension.

#This is implemented using PIL which is a bit lengthy because we are working on numpy arrays where the pixels are floating-point values. This is not supported by PIL so the image must be converted to 8-bit bytes while ensuring the pixel-values are within the proper limits. Then the image is resized and converted back to floating-point values.

def resize_image(image, size=None, factor=None):
    # If a rescaling-factor is provided then use it.
    if factor is not None:
        # Scale the numpy array's shape for height and width.
        size = np.array(image.shape[0:2]) * factor
        
        # The size is floating-point because it was scaled.
        # PIL requires the size to be integers.
        size = size.astype(int)
    else:
        # Ensure the size has length 2.
        size = size[0:2]
    
    # The height and width is reversed in numpy vs. PIL.
    size = tuple(reversed(size))

    # Ensure the pixel-values are between 0 and 255.
    img = np.clip(image, 0.0, 255.0)
    
    # Convert the pixels to 8-bit bytes.
    img = img.astype(np.uint8)
    
    # Create PIL-object from numpy array.
    img = PIL.Image.fromarray(img)
    
    # Resize the image.
    img_resized = img.resize(size, PIL.Image.LANCZOS)
    
    # Convert 8-bit pixel values back to floating-point.
    img_resized = np.float32(img_resized)

    return img_resized

########################################################################



########################################################################