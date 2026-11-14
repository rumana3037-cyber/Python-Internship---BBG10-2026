height_cm = "175"
weight_kg = "68.5"

# Convert strings to float and height from cm to meters
height_m = float(height_cm) / 100
weight_kg = float(weight_kg)

# Calculate BMI
BMI = weight_kg / (height_m * height_m)
print("BMI:", round(BMI, 2))