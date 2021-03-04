#Shipping Accounts App

#Define list of users
users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj', 'eliasro']
print("Welcome to the Shipping Accounts Program.")

#Get user input
username = input("\nHello, what is your username: ").lower().strip()

#User is in list.... 

if username in users:
    #print a price summary
    print("\nHello " + username + ". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100: \t\t$5.10 each")
    print("Shipping orders 100 to 500: \t\t$5.00 each")
    print("Shipping orders 500 to 1000 \t\t$4.95 each")
    print("Shipping orders over 1000: \t\t$4.80 each")

    #Determine price based on how many items are shipped
    quantity = int(input("\nHow many items would you like to ship: "))
    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80
    #Display final cost
    bill = quantity*cost
    bill = round(bill, 2)
    print("To ship " + str(quantity) + " items it will cost you $" +str(bill) + " at $" + str(cost) + " per item.")
    
    #Place order
    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
        print("OKAY. Shipping your " + str(quantity) + " items.")
    else:
        print("OKAY, no order is being placed at this time.")

#The user is not in the list
else:
    print("Sorry, you do not have an account with us. Goodbye...")