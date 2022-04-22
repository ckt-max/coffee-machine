# coffee-machine
Code for a coffee machine

# Functions of the coffee machine in their respective order:

1. Prompts user by asking “ What would you like to have? (espresso/latte/cappuccino): ”
2. Turns off the Coffee Machine by entering “ off ” to the prompt.
3. Prints report : When the user enters “report” to the prompt, a report is generated that shows
   the current resource values. Example,
    water: 100 ml
    milk: 50 ml
    coffee: 76 ml
    profit: $2.5
4. Check resources sufficient?: 
  - The check() function checks if the available resources are enough for making the required drink.
  - E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It does
    not continue to make the drink but prints: “ Sorry there is not enough water. ”
5. Processes coins according to their values and calculates the money received
6. Check transaction successful?
  - Checks if the user has inserted enough money to purchase the drink they selected.
    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    program should say “ Sorry that's not enough money. Money refunded. ”.
  - If the user has inserted too much money, the machine offers change
7. Make Coffee: If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink is deducted from the
    coffee machine resources.
    - The update() function is used to update the resources, while profit variable is updated by adding the cost of the drink to it
    E.g. report before purchasing latte:
    water: 300ml
    milk: 200ml
    coffee: 100g
    profit: $0
    Report after purchasing latte:
    water: 100ml
    milk: 50ml
    coffee: 76g
    money: $2.5
 8. Once all resources have been deducted, it tells the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink.
  
