#Hamburger Salad ordering program

#Variables:
order = (str(input("Enter order: ")))

#Function definition:

def item_order(order):
    """Assumes string of input, with words separated by one space, Returns item:#"""
    order.split(" ")
    hamburger = order.count("hamburger")
    salad = order.count("salad")
    water = order.count("water")
    for item in order:
        order.count("hamburger")
        order.count("salad")
        order.count("water")
    print("salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" + str(water))


#Call the function:

item_order(order)


#Tests

TestArray = ["hamburger water salad", "hamburger hamburger hamburger", "water water water", "salad salad salad", "alakjdfalkjajjnsdjfh", "hamburgerwatersalad", "654354134586"]
AnswerArray = [] 
