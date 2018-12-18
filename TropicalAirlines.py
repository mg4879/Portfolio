
def calcTrip(getCustomerName):
    """The calcTrip function calculates the trip and destination costs based on input from getTrip and getDestinaton.
    After the user has selected a trip type and destination, the function then calls the calcClass, calcSeat,
    and calcAge functions to calculate the other ticket choices and totals. Once the functions have returned the values
    back to calcTrip, the final total cost is calculated and returns the value back to the Main function."""

    CAIRNSONEWAY = 250
    SYDNEYONEWAY = 420
    PERTHONEWAY = 510
    CAIRNSRETURN = 400
    SYDNEYRETURN = 575
    PERTHRETURN = 700

    getTicketName = input(str(getCustomerName) + " " + "is this ticket for\n(Y)ou\n(S)omeone else\n").upper()

    while getTicketName != "Y" and getTicketName != "S":  # Error handling
        print("Invalid Menu Choice\n")
        getTicketName = input(str(getCustomerName) + " " + "is this ticket for\n(Y)ou\n(S)omeone else\n").upper()

    if getTicketName == "S":  # Prompts the user to enter the passenger's name if ticket is not for customer.
        getPassengerName = input("Please enter the passenger's name: ")

        while getPassengerName == "":  # Error handling
            print("\nInvalid input\n")
            getPassengerName = input("Please enter the passenger's name: ")

        getCustomerName = getPassengerName

    getTrip = input("\nIs this a (O)ne way trip or (R)eturn trip\n").upper()

    while getTrip != "O" and getTrip != "R":
        print("Invalid Input")
        getTrip = input("\nIs this a (O)ne way trip or (R)eturn trip\n").upper()

    if getTrip == "O":
        getDestination = input("Please choose a One Way destination\n" +
                               "(C)airns - $250\n(S)ydney - $420\n(P)erth  - $510\n ").upper()

        while getDestination != "C" and getDestination != "S" and getDestination != "P":  # Error handling
            print("Invalid selection")
            getDestination = input("\nPlease choose a One Way destination\n" +
                                   "\n(C)airns - $250\n(S)ydney - $420\n(P)erth - $510\n").upper()

        if getDestination == "C":
            destinationName = "Cairns One Way"
            destinationCost = CAIRNSONEWAY

        elif getDestination == "S":
            destinationName = "Sydney One Way"
            destinationCost = SYDNEYONEWAY

        else:
            destinationName = "Perth One way"
            destinationCost = PERTHONEWAY

    else:  # Calculates the Return ticket destination cost
        getDestination = input("\nPlease choose a Return destination" +
                               "\n(C)airns - $250\n(S)ydney - $420\n(P)erth  - $510\n").upper()

        while getDestination != "C" and getDestination != "S" and getDestination != "P":  # Error handling
                print("Invalid selection")
                getDestination = input("\nPlease choose a Return destination:" +
                                       "\n(C)airns - $250\n(S)ydney - $420\n(P)erth  - $510\n").upper()

        if getDestination == "C":
            destinationName = "Cairns Return"
            destinationCost = CAIRNSRETURN

        elif getDestination == "S":
            destinationName = "Sydney Return"
            destinationCost = SYDNEYRETURN

        else:
            destinationName = "Perth Return"
            destinationCost = PERTHRETURN

    classFare, className = calcClass()
    seatFee, seatName = calcSeat()
    ticketCost = destinationCost + classFare + seatFee
    ageDiscount, ageName, displayAge = calcDiscount(ticketCost)
    totalCost = (ageDiscount)

    print("\nCalculating Fare.....\n")
    print("The ticket for", getCustomerName, "is: ")
    print(destinationName, "\t" + '${:,.2f}'.format(destinationCost))
    print(className, "\t" + '${:,.2f}'.format(classFare))
    print(seatName, "\t" + '${:,.2f}'.format(seatFee))
    print("Age" + "\t\t\t\t" + str(displayAge) + str(ageName))
    print("Total Price: ", "\t" + '${:,.2f}'.format(totalCost)+ "\n")
    return totalCost


def calcClass():
        """This function calculates the class cost of the ticket based on user input from getClass.Once a class choice
        is selected the function returns the class cost and clas name values selected by the user to the
        calcTrip function."""

        BUSINESSCLASSCOST = 275
        ECONOMYCLASSCOST = 25
        FRUGAL = 0
        BUSINESSCLASS = "Business Class"
        ECONOMYCLASS = "Economy Class"
        FRUGALCLASS = "Frugal Class"
        getClass = input("Please choose a class\n(B)usiness - $275\n(E)conomy  - $90\n(F)rugal   - $25 \n").upper()

        while getClass == "" or getClass != "B" and getClass != "E" and getClass != "F":  # Error handling
            print("Invalid selection\n")
            getClass = input("Please choose a class\n(B)usiness - $275\n(E)conomy  - $90\n(F)rugal   - $25 \n").upper()

        if getClass == "B":
            classCost = BUSINESSCLASSCOST
            className = BUSINESSCLASS

        elif getClass == "E":
            classCost = ECONOMYCLASSCOST
            className = ECONOMYCLASS

        else:
            classCost = FRUGAL
            className = FRUGALCLASS

        return classCost, className


def calcSeat():
    """This function calculates the seat cost of the ticket based user input from getSeat. The function returns the
    seat name and seat cost values to the calcTrip function."""

    WINDOWSEATCOST = 75
    AISLESEATCOST = 50
    MIDDLESEATCOST = -25
    WINDOWSEAT = "Window Seat"
    AISLESEAT = "Aisle Seat\t"
    MIDDLESEAT = "Middle Seat"

    getSeat = input("\nPlease choose a seat\n(W)indow - $75\n(A)isle  - $25\n(M)iddle - $0 \n").upper()

    while getSeat != "W" and getSeat != "A" and getSeat != "M": # Error handling
        print("Invalid selection\n")
        getSeat = input("Please choose a seat\n(W)indow - $75\n(A)isle  - $25\n(M)iddle - $0 \n").upper()

    if getSeat == "W":
        seatCost = WINDOWSEATCOST
        seatName = WINDOWSEAT

    elif getSeat == "A":
        seatCost = AISLESEATCOST
        seatName = AISLESEAT

    else:
        seatCost = MIDDLESEATCOST
        seatName = MIDDLESEAT
    return seatCost, seatName


def calcDiscount(ticketCost):
    """This function calculates a 50% discount on the tickets total cost based on the age entered in getAge. If the age
       entered is 15 and under the discount is applied to the total cost of the ticket, otherwise no discount will be
       applied to the total cost. The function returns the discount fare and discount status back to calcTrip."""

    CHILDFARE = ticketCost * 0.50
    getAge = int(input("Please enter the Passengers age" +
                       "(Passengers under 16 will receive a 50% off child fare discount \n"))

    while getAge != int and getAge < 0 or getAge > 125:  # Error handling to ensure age is in valid range
        print("Invalid age")
        getAge = int(input("Please enter your age \n"))

    if getAge >= 0 and getAge <= 15:
        discountName = "(Eligible for a child ticket, 50% discount applied)"
        discountFare = CHILDFARE
    else:
        discountName = "(Not eligible for a child ticket, No discount applied)"
        discountFare = ticketCost
    return discountFare, discountName, getAge


def main():
    """The Main function is the starting point of the program. The user is asked to enter their name and is welcomed
    to the program. getChoice prompts the user to make a menu selection, if the user enters an invalid selection
    they are prompted to make another selection until a valid one is made. The (I) option displays the airlines
    information to the user afterwards prompting the user to choose another option. The (O) option calls the calcTrip
    function and returns the values to main appending them to the pricesList to be displayed at the end of the program.
    The (E) option exits the program displaying any orders made by the user as well as the final total cost."""

    pricesList = []
    getCustomerName = input("What is your name?: ")

    while getCustomerName == "":  # Error handling
        print("\nInvalid Name\n")
        getCustomerName = input("Please enter your name: ")

    print("\nWelcome",getCustomerName + ".")
    print("\nTropical Airlines Ticket Ordering System\n")
    getChoice = input("Please make a selection\n\t(I)nformation\n\t(O)rder a ticket\n\t(E)xit the program: ").upper()

    while getChoice != "E":  # Error handling

        if getChoice == "I":
            print("\nThank you for choosing Tropical Airlines for your air travel needs.\n"
                  "You will be asked questions regarding what type of ticket you would like to purchase\n"
                  "as well as destination information. We also offer 50% discounted fares for children.\n")

        elif getChoice == "O":
            total = calcTrip(getCustomerName)
            pricesList.append(total) # Appends orders placed by user to a list

        else:
            print("\nInvalid Menu Choice\n")
        print("Tropical Airlines Ticket Ordering System")
        getChoice = input("\nPlease make another selection:\n" +
                          "\t(I)nformation\n\t(O)rder a ticket\n\t(E)xit the program: ").upper()

    pricesList.sort()  # Sorts the ticket order totals in the list from smallest to largest
    finalCost = sum(pricesList)

    if len(pricesList) == 0:
        print("\nYou did not purchase any tickets\n")

    elif len(pricesList) == 1:
        print("\n",getCustomerName + " " + "your total is", '${:,.2f}'.format(pricesList[0]), "and your final total is ", '${:,.2f}'.format(finalCost))
    else:
        print(getCustomerName + " " + "Your orders are")
        for i in pricesList:
            print(i)
        print("and your final total is", '${:,.2f}'.format(finalCost))
    print("Thank you for choosing Tropical Airlines.")

main()
