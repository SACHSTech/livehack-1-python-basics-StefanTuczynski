"""
Name:   problem2.py
Purpose: This problem requires the amount of chicken needed to distrubute to the 
number of students + Mr. Fabroa (who gets the remaining pieces). This code will
calculate the number of wings to fairly distribute to each classmate, but also
Mr. Fabroa who recieves the rest.

Author: Tuczynski.S

Date:   07/12/2020
"""

#input data for amount of chicken pieces
chicken = int(input("How many pieces of chicken are there: "))
students = int(input("How many students are there: "))

#computes data given by user and applies it to the problem
distributed_pieces = round((chicken / students))
fabroas_pieces = (chicken % students)

#outputs the pieces each student gets and the pieces Mr.Fabroa gets
print("Each student gets:", distributed_pieces, "and Mr.Fabroa gets:", fabroas_pieces)

