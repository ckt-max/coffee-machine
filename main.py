MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Check resources sufficient?


def check (button):
    ing = MENU[button]['ingredients']
    flag = 0
    count = 0

    for a, b in ing.items():
        count += 1
        if b <= resources[a]:
            flag += 1
        else:
            print('Sorry there is not enough '+ a)
    if flag == count:
        return 1

    else:
        return 0


def update(button):
    ing = MENU[button]['ingredients']

    for a, b in ing.items():
        resources[a] -= b

##################################################
# asking user
state = 1
while state == 1:
    button = input("\n\nWhat would you like to have? \n  Espresso\n  Latte\n  Cappuccino \n")

    ## turning the machine off

    if button == 'off': ( exit() )

    ## print report
    elif button == 'report':
        for a,b in resources.items():
            print(a+': '+str(b)+' ml')
        print('profit: '+str(profit))
    # checking resources
    ## process coins if resources sufficient

    elif check(button) == 1:
        print('The cost of your drink is ' + str(MENU[button]['cost']) + '\nInsert the coins')
        quarters = int(input('no of quarters'))
        dimes = int(input('No of dimes'))
        nickels = int(input('No of nickels'))
        pennies = int(input('No of pennies'))

        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

        if total >= MENU[button]['cost']:
            print('\nTransaction successful')

            if total > MENU[button]['cost']:
                print('Here is your change - ' + str(total - MENU[button]['cost']))

            # updating money and resources after transaction
            profit += MENU[button]['cost']
            update(button)

            # acknowledgement
            print('Here is your '+button+' Enjoy!')
        else:
            print('Sorry that is not enough money. Money refunded.')






