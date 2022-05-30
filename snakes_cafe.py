intro_message = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""

order_intro = """
***********************************
** What would you like to order? **
***********************************
"""

print(intro_message)
print(menu)

menu_list = ["Wings", "Cookies", "Spring Rolls",
             "Salmon", "Steak", "Meat Tornado", "A Literal Garden",
             "Ice Cream", "Cake", "Pie",
             "Coffee", "Tea", "Unicorn Tears"]


ordered = {}

print(order_intro)
while True:

    order = input("> ")
    if order in menu_list:
        if order in ordered:
            ordered[order] = ordered.get(order) + 1
        else:
            ordered[order] = 1
        order_input = "** {} order of {} have been added to your meal **"
        # num = ordered.count(order)
        print(order_input.format(ordered[order], order))
        continue
    elif order == "quit":
        break
    else:
        print(f'Sorry, {order} not in the menu')
        continue

str_final = "Your order is: "
for item in ordered:
    str_final += f"{ordered.get(item)} {item},"

final_order = str_final[:-1] + "."

print(final_order)

