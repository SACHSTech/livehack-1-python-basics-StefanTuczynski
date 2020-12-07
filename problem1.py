"""
Name:   problem1.py
Purpose: This problem requires a celsius to fahrenheit converter to help the user 
understand the amount of degrees celsius to fahrenheit


Author: Tuczynski.S

Date:   07/12/2020
"""

#inputs user data for the amount of degrees celsius
print("--- Welcome to the online celsius to fahrenheit converter ---")
c = float(input("Degrees Celsius: "))

#computes the amount of degrees celsius to amount of degrees fahrenheit
f = (c * (9/5) + 32)

#outputs the amount of degrees fahrenheit after conversion
print(c , "degrees celsius equals", f, "degrees fahrenheit.")
print("--- Thank you for using the online fahrenheit to celsius conveter! ---")
