import math

# This example uses the following python functions
# input() function
# integers int()
# math

# Read the radius from a user.
# Write a formula for surface area and volume of a sphere.
# Formula for Radius of a sphere Area (4πr2)
# Formula for Volume of a sphere Area V= 4/3(πr3)
# Print values using a print statement.

print("Calculate Volume of a sphere")
sphere_radius = input("Enter radius \n")  # Note inputs are now in the form of a string
sphere_radius = int(sphere_radius)  # Convert it to integer before multiplying
sphere_radius = (4 * (math.pi * (math.pow(sphere_radius, 2))))
print("The Volume of the sphere is: ")
print(round(sphere_radius, 2))
print("\n")

print("Calculate Area of a sphere")
sphere_area = input("Enter radius \n")  # Note inputs are now in the form of a string
sphere_area = int(sphere_area)  # Convert it integer before multiplying (4 / 3 * (math.pi * (math.pow(sphere_area, 3))))
sphere_area = (4 / 3 * (math.pi * (math.pow(sphere_area, 3))))
print("The Area of the sphere is: ")
print(round(sphere_area, 2))
