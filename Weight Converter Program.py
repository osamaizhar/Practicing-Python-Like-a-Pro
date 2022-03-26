#    ** Project Weight Converter ** 

# Create a program that converts a person weight from pounds to kilograms and vice versa
# depending on user input
# user can select whether to enter their weight in pounds or kilograms
# Output is converted weight with units 
# Hint: 1kg = 2.20462 pound




user_sel = input("Please select (k) for kg and (p) for pounds: ").lower()
if user_sel=="p" or user_sel=="k":

    weight = float(input("Enter your weight for conversion: "))   

    if user_sel=="p":# for pounds => kg
        weight/=2.20462 # weight = weight/2.20462
        print(f'Your weight in kilograms is {weight} kg')

    if user_sel =="k": # for kg => pounds
        weight*=2.20462 # weight = weight*2.20462
        print("Your weight in pounds is:",weight,"pounds")
   
else:
    print("Invalid statement,please enter either p for pounds or k for kilograms")












