"""
Soumen Nath
ICS4U
SoumenNath_movieSystem.py
Description: The program allows customers to purchase tickets to view available movies at The ByTowne Cinema.
The customers are allowed to select a movie and a date to view the movie. They can then select the type and number
of tickets to purchase, along with reserving seats.
"""
#module to use clear screen
import os
#3D list for available seats during the six different days
seats = [[[' \t', 'O\t', 'O\t', 'O\t','O\t', 'O\t', 'O\t', 'O'] for i in range(6)] for i in range(6)]
#global variables
cost = 0; counter1 = 0; counter2 = 0; counter3 = 0; numPeople = 0; dateChoice = 0
uName = ''; pWord = ''; accounts = []; member = False
#Menu function
def menu():
    global member
    #Print following statements
    print('\t\t\t\t\t--------------------------------------\n\t\t\t\t\tWelcome to ByTowne Cinema Ticket Booth\n\t\t\t\t\t--------------------------------------')
    print('Please select an option:\nSign In\t\t\t1\nCreate Account\t\t2\nUse Guest Account\t3')
    print('\n**Creating an account will result in being availbe to purchase cheaper tickets\nthat are only availble to Bytowne members for only a small montly fee.')
    print('So sign up now to start saving!**\n')
    #Accepting user input
    accountType = int(input('Please enter your decision: '))
    while accountType< 1 or accountType>3:
        accountType = int(input('Error! The number you entered is out of the range.\nPlease enter your decision: '))
    #Preventing the first user from using a non existent account
    while len(accounts) == 0 and accountType == 1:
        print()
        accountType = int(input('Error! You do not have an account! So sign up or use a guest account\nPlease enter your decision: '))
    #Allow the user to sign in if he/she has an account
    if accountType == 1:
        uName = input('Please enter your username: ')
        pWord = input('Please enter your password: ')
        for i in range(len(accounts)):
            while uName != accounts[i]:
                uName = input('Error! The username you entered does not exist! Please enter your username: ')
            while uName == accounts[i] and pWord != accounts[i+1]:
                pWord = input('Error! The password you entered does not exist!\nPlease enter your password: ')
            if uName == accounts[i] and pWord == accounts[i+1]:
                print('Welcome back', uName)
                member = True
                input('')
                break
    #Allow the user to create an account and become a member
    elif accountType == 2:
        uName = input('Please enter a username: ')
        for names in accounts:
            while uName == names:
                uName = input('Error! That username already exists.\nPlease enter a username: ')
        pWord = input('Please enter a password: ')
        accounts.append(uName)
        accounts.append(pWord)
        member = True
#Function to let user choose one of the following movies and select a date to view the movie at
def movieSelection():
    global dateChoice
    os.system('cls')
    print('\nMovie\t\t\t\t\tChoice Number\nThree Billboards Outside Ebbing\t\t1\nThe Dark Knight\t\t\t\t2\nSaving Private Ryan\t\t\t3')
    movieChoice = int(input('Please enter your selection: '))
    while movieChoice <1 or movieChoice>3:
        movieChoice = int(input('Error! Please enter your selection: '))
    if movieChoice == 1:
        print('\nAvailable Dates\t\t\tChoice Number\nMarch 13, 2018\t\t\t1\nMarch 14, 2018\t\t\t2')
        dateChoice = int(input('Please enter your selection: '))
        while dateChoice != 1 and dateChoice != 2:
            dateChoice = int(input('Error! Please enter your selection: '))
    elif movieChoice == 2:
        print('\nAvailable Dates\t\t\tChoice Number\nMarch 15, 2018\t\t\t3\nMarch 16, 2018\t\t\t4')
        dateChoice = int(input('Please enter your selection: '))
        while dateChoice != 3  and dateChoice != 4:
            dateChoice = int(input('Error! Please enter your selection: '))
    elif movieChoice == 3:
        print('\nAvailable Dates\t\t\tChoice Number\nMarch 17, 2018\t\t\t5\nMarch 18, 2018\t\t\t6')
        dateChoice = int(input('Please enter your selection: '))
        while dateChoice != 5 and dateChoice != 6:
            dateChoice = int(input('Error! Please enter your selection: '))
#Function to allow user to buy the tickets
def buyingTickets():
    os.system('cls')
    #Indicating to the function to use the global variables
    global cost; global counter1; global counter2; global counter3; global numPeople
    decision = 'y'
    #Loop to keep letting the user purchase tickets
    while decision == 'y':
        numTickets = 0
        print('\nTicket Price\t\t\t\tChoice Number\n$12.00 for non-members\t\t\t1\n$8.00 for ByTowne Members (with card)\t2\n$6.00 for children under 12\t\t3')
        ticketChoice = int(input('Please enter your selection: '))
        #Preventing users that aren't members from buying tickets that are member exclusive
        while (ticketChoice<1 or ticketChoice>3) or (ticketChoice == 2 and member == False):
            ticketChoice = int(input('Error! Please enter your selection again: '))
        numTickets = int(input('Please enter the number of tickets to purchase: ' ))
        numPeople += numTickets
        #Calculates cost
        if ticketChoice == 1:
            cost += 12.00 * numTickets
            counter1 += 1 * numTickets
        elif ticketChoice == 2:
            cost += 8.00 * numTickets
            counter2 += 1 * numTickets
        elif ticketChoice == 3:
            cost += 6.00 * numTickets
            counter3 += 1 * numTickets
        decision = input('Would you like to purchase additional tickets? (y/n): ')
    print('You have purchased', numTickets, 'tickets')
#Function to allow the user to choose available seats
def choosingSeats():
    os.system('cls')
    print('\nPlease choose your seats.\nAvailable seats are marked with O, taken seats are marked with an X.')
    value = 0
    #Following loops write the numbers 1-7 on the first row and 1-5 on the first column for each table
    for j in range(6):
        for column in range(1, 8):
            value += 1
            seats[j][0][column] = str(value) + ('\t')
        value = 0
    for k in range(6):
            for row in range (1, 6):
                value += 1
                seats[k][row][0] = str(value) + ('\t')
            value = 0
    #Display the table of seats for the specific date the user has chosen
    for row in range (6):
        for column in range(8):
            print(seats[dateChoice-1][row][column], end='')
        print('')
    #Allow the user to pick the number of seats based on the number of tickets purchased
    for n in range(numPeople):
        row = int(input('Please enter the number for the row of the desired seat: '))
        while row <1 or row>5:
            row = int(input('Error, that row does not exist!\nPlease enter the number for the row of the desired seat: '))
        column = int(input('Please enter the number for the column of the desired seat: '))
        while column <1 or column>7:
            column= int(input('Error, that column does not exist!\nPlease enter the number for the column of the desired seat: '))
        #Prevents the user from reserving a seat that is already taken
        while seats[dateChoice-1][row][column] == 'X\t':
            row = int(input('That seat is already taken!\nPlease enter the number for the row of the desired seat: '))
            while row <1 or row>5:
                row = int(input('Error, that row does not exist!\nPlease enter the number for the row of the desired seat: '))
            column = int(input('Please enter the number for the column of the desired seat: '))
            while column <1 or column>7:
                column= int(input('Error, that column does not exist!\nPlease enter the number for the column of the desired seat: '))
        #Fill the reserved seat with an X and display it to the user
        seats[dateChoice-1][row][column] = 'X\t'
        for row in range (6):
            for column in range(8):
                print(seats[dateChoice-1][row][column], end='')
            print('')
        print('Your seats have been reserved!')
        input('')
#Function to let the user pay for the tickets
def payMent():
    os.system('cls')
    #Counters indicate how many of each type of ticket was purchased
    if counter1> 0:
        print(counter1,'- non member @ $12.00')
    if counter2 >0 :
        print(counter2,'- Bytowne Member @ $8.00')
    if counter3> 0:
        print(counter3,'- childlren @ $6.00')
    print('Subtotal: $'+ str(format(cost, '.2f')))
    #Calculate tax and the total Price
    tax = 0.13 * cost
    total = 1.13 * cost
    #Allows the user to enter coupon codes
    coupon = input('Do you have a coupon code? If not then press A. (Mr. Hughes please view the comments for the codes)\nIf yes then enter the code here: ')
    while coupon !='A' and coupon != '12ab' and coupon != 'xll3' and coupon != '455q':
            coupon = input('Error! Please press A or enter a coupon code: ')
    if coupon == '12ab':
        print('Discount: $5.00')
        total  -= 5
    elif coupon  == 'xll3':
        print('Discount: $4.00')
        total  -= 4
    elif coupon == '455q':
        print('Discount: $3.00')
        total  -= 3
    #Display the bill to the user
    print('Tax: $'+ str(format(tax, '.2f')))
    print('Total: $'+ str(format(total, '.2f')))
    print('Your credit card has been charged the above total. The charge will be from ByTowne Cineplex. Enjoy your viewing experience!')
    input('')
    #Clearing the screen
    os.system('cls')
    main()
def main():
    #Resetting variable values
    global member; global cost; global numPeople; global counter1; global counter2; global counter3
    member = False; cost = 0; counter1 = 0; counter2 = 0; counter3 = 0; numPeople = 0
    print('\t\t\t\t\t--------------------------------------\n\t\t\t\t\tWelcome to ByTowne Cinema Ticket Booth\n\t\t\t\t\t--------------------------------------')
    print('Please select an option:\nPurchase tickets\t1\nExit the program\t2')
    uDecision = int(input('Please enter your decision: '))
    while uDecision != 1 and  uDecision != 2:
        uDecision = int(input('Error! The number you entered is out of the range.\nPlease enter your decision: '))
    while uDecision == 1:
        os.system('cls')
        #Running the following fuctions:
        menu()
        movieSelection()
        buyingTickets()
        choosingSeats()
        payMent()
    while uDecision == 2:
        os.system('cls')
        print('Thank you for using this program!')
        input('')
        exit()
main()
