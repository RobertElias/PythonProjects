# Create an application that converst temperature
# from celcius to degrees

print("Welcome to the Temperature Conversion Program.")

#Gather user input

temp_f = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

#Convert temperature celcius into fahrenheit
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

# Round the temperatures
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

#Summary table
print("\nDegrees Fahreneheit:\t" + str(temp_f))
print("Degrees Celsius:\t" + str(temp_c))
print("Degrees Kelvin:\t\t" + str(temp_k))
