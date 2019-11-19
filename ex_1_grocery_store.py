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


# EXAMPLE 1 - Basic Example
# Variables holding the prices of the six items:

penne = 16.68  # penne 16 oz, pack of 12
arrabiata = 6.98  # Arrabiata sauce 24oz
garlic = 16.78   # 20 pack garlic clove
seasoning = 15.26   # Italian Seasoning
baguettes = 3.00   # Baguette twin pack
meatballs = 4.39   # 12 oz bag of meatballs


# Function sum_total
# A subtotal is the sum of all prices before any sales taxes or discounts are added.
def sum_total(penne, arrabiata, garlic, seasoning, baguettes, meatballs):
    subtotal = penne + arrabiata + garlic + seasoning + baguettes + meatballs
    print(round(subtotal, 2))
    return

sum_total(penne, arrabiata, garlic, seasoning, baguettes, meatballs)

# Output
# 63.09


# EXAMPLE 2 - Function using append() and sum() function to add items to list. 
# Note: append() only takes parameter
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

grocery_list = []  # empty grocery list

def sum_list(penne, arrabiata, garlic, seasoning, baguettes, meatballs):
    grocery_list.append(penne)
    grocery_list.append(arrabiata)
    grocery_list.append(garlic)
    grocery_list.append(seasoning)
    grocery_list.append(baguettes)
    grocery_list.append(meatballs)
    sub_total = sum(grocery_list)
    print(round(sub_total, 2))
    return

sum_list(penne, arrabiata, garlic, seasoning, baguettes, meatballs)

# Output
# 63.09


# EXAMPLE 3 - Function Using extend() and sum() function to to add items to list.
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

grocery_list_2 = []  # empty grocery list

def sum_list2(penne, arrabiata, garlic, seasoning, baguettes, meatballs):

    new_list = [penne, arrabiata, garlic, seasoning, baguettes, meatballs];
    grocery_list_2.extend(new_list)  # add items to grocery list
    sub_total = sum(grocery_list_2)
    print(round(sub_total, 2))
    return

sum_list2(penne, arrabiata, garlic, seasoning, baguettes, meatballs)

# Output
# 63.09
