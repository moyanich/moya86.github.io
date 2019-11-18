# Programming Challenge: Grocery Store Purchase
# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
# Penne 16 oz Pack of 12 - $16.68
# Arrabiata Pasta Sauce 24 oz - $6.98
# Bag of 20 Organic Garlic Cloves - $16.78
# Italian Seasoning 1.5 oz Bottle - $15.26
# Artisan Baguettes Twin Pack - $3.00
# 12 oz Bag of Meatballs - $4.39
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.
# The subtotal is just the sum of all of their prices.
# Use print() to display the result of the expression.


# Variables holding the prices of the six items:
penne = 16.68  # penne 16 oz, pack of 12
arrabiata = 6.98  # Arrabiata sauce 24oz
organic_garlic_cloves = 16.78   # 20 pack garlic clove
italian_seasoning = 15.26   # Italian Seasoning
artisan_baguettes_twin_pack = 3.00   # Baguette twin pack
meatballs = 4.39   # 12 oz bag of meatballs


# Function sum_total
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

def sum_total(penne, arrabiata, organic_garlic_cloves, italian_seasoning, artisan_baguettes_twin_pack, meatballs):
    subtotal = penne + arrabiata + organic_garlic_cloves + italian_seasoning + artisan_baguettes_twin_pack + meatballs
    print(round((subtotal), 2))
    return

sum_total(penne, arrabiata, organic_garlic_cloves, italian_seasoning, artisan_baguettes_twin_pack, meatballs)

# Output
# 63.09