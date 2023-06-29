import numpy as np

# Set the values for focal length and image center according to your requirements
focal_length_x = 500  # Focal length in pixels along the x-axis
focal_length_y = 500  # Focal length in pixels along the y-axis
image_center_x = 320  # X-coordinate of the image center in pixels
image_center_y = 240  # Y-coordinate of the image center in pixels

# Define the camera matrix
camera_matrix = np.array([[focal_length_x, 0, image_center_x],
                          [0, focal_length_y, image_center_y],
                          [0, 0, 1]])

np.save("camera_matrix.npy", camera_matrix)
