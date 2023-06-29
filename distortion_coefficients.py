import numpy as np

# Set the values for distortion coefficients according to your requirements
k1 = 0.1  # Radial distortion coefficient k1
k2 = 0.2  # Radial distortion coefficient k2
p1 = 0.01  # Tangential distortion coefficient p1
p2 = -0.02  # Tangential distortion coefficient p2
k3 = 0.001  # Radial distortion coefficient k3


# Define the distortion coefficients
distortion_coeffs = np.array([k1, k2, p1, p2, k3])

np.save("dist_coeffs.npy", distortion_coeffs)
