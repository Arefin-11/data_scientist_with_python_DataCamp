# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Create a numpy array from height_in: np_height_in
np_height_in=np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m=np_height_in*0.0254

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb)*0.453592

# Calculate the BMI: bmi

bmi=np_weight_kg/np_height_m**2
# Print out bmi
print(bmi)

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light=bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[bmi<21])

