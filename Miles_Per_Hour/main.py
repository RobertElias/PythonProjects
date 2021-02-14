# create a function that changes mph to meters per second

print("Welcome to the MPH to MPS Conversion App.")


mph = float(input("\nWhat is your speed in miles per hour: "))

#Convert to MPS
mps = mph * 0.4474 
#round the mps
mps = round(mps, 2)

print("Your speed in meters per second is " + str(mps) + ".")