#Exercise 1#

pet_list = ['Kira','Lola', 'Max', 'Nika']
my_friends = ('Alberto', 'Raquel', 'Sheila', 'Ander')
price_float = 12.99
sales_int = 428

from decimal import Decimal

price_decimal = Decimal(price_float)

family = {
    "grandma": "Rose Marie",
    "mom": "Rose",
    "dad": "Rosmund",
    "cousin": "Rick",
}

#Exercise 2#

import math

price_float = 12.49
round_up_price = math.ceil(price_float)
print(round_up_price)

#Exercise 3#

square_root_prince = math.sqrt(price_float)
print(square_root_prince)

#Exercise 4#

my_grandma = family["grandma"]
print(my_grandma)

#Exercise 5#

second_friend = my_friends[1]
print(second_friend)

#Exercise 6#

pet_list.append('Golfo')
print(pet_list)

#Exercise 7#

pet_list[0] = 'Panda'
print(pet_list)

#Exercise 8#

pet_list.sort()
print(pet_list)

#Exercise 9#

my_friends += ('Sandra',)
print(my_friends)