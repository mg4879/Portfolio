# This program allows the user to input the weight amount for a package to be shipped and displays the cheapest
# shipping option available


print("------Cheapest shipping option calculator------\n")
# user enters the amount for weight

try:
    weight = float(input("Please enter the weight of the package to be shipped: "))
except ValueError:
    print("\nError: invalid input\nPlease enter weight in decimal format\n")
    weight = float(input("Please enter the weight of the package to be shipped: "))

# this function calculates the cost for ground shipping
def shipping_cost_ground(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif weight <= 6:
        price_per_pound = 3.00
    elif weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75
    return 20 + (price_per_pound * weight)


# premium shipping cost
shipping_cost_premium = 125.00


# this function takes the weight entered by the user and calculates the cost for shipping via drone
def shipping_cost_drone(weight):
    if weight <= 2:
        price_per_pound = 4.50
    elif weight <= 6:
        price_per_pound = 9.00
    elif weight <= 10:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25
    return price_per_pound * weight


def print_cheapest_shipping_method(weight):
    ground = shipping_cost_ground(weight)
    premium = shipping_cost_premium
    drone = shipping_cost_drone(weight)

    if ground < premium and ground < drone:
        method = "standard ground"
        cost = ground
    elif premium < ground and premium < drone:
        method = "premium ground"
        cost = premium
    else:
        method = "drone"
        cost = drone
    print("\nThe cheapest option available is $%.2f with %s shipping." % (cost, method))


print_cheapest_shipping_method(weight)
