# LISTS ===================
'''
import random
import sys

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D","7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input=input("Press enter to pick a card, or Q to quit")
    if user_input in ["Q","q"]: break
    card=random.choice(diamonds)
    hand.append(card)
    diamonds.remove(card)
    print("Ramaining Cards: ",diamonds)
    print("Your Hand: ",hand)

if not diamonds:
    print('There are no more cards to pick.')
    sys.exit()
'''

'''
my_string = "phone"

print(my_string[0:-2])
Outputs: "pho"
# my_string[-2] is "n" which is not included but the element left of it is

print(my_string[-3:-1])
Outputs: "on"
# Starts at my_string[-3] which is "o" and ends at my_string[-1] which is "e" but it is not inclusive at the end so the final output is just "on"
'''


# DICTIONARIES ==========
'''inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall (inches_snow) :
    total_inches=0
    for day,inches in inches_snow.items():
        total_inches+=int(inches)
    print('Total snowfall inches ',total_inches)

print_total_snowfall(inches_snow)

thur_snow=input("How many inches of snow fell on Thursday?")
inches_snow["Thursday"]=thur_snow or 0
print_total_snowfall(inches_snow)
'''