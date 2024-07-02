import artcoffee
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0
def is_sufficient(ingredients_of_order):
    for item in ingredients_of_order:
        if ingredients_of_order[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please enter the coins:")
    total=int(input("how many quarters?:"))*0.25
    total+=int(input("how many dimes?:"))*0.1
    total+=int(input("how many nickels?:"))*0.05
    total+=int(input("how many pennies?:"))*0.01
    return total

def transaction_completed(money_entered, drink_ordered):
    if money_entered>=drink_ordered:
        change=round(money_entered-drink_ordered,2)
        print(f"Here is your change:${change}")
        global money
        money+=drink_ordered
        return True
    else:
        print("Sorry money entered is insufficient. Your money is refunded")
        return False   
def making_coffee(name_of_drink, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {name_of_drink}, have a good time!")    

is_on=True
while is_on:
    print(artcoffee.logo)
    print("What would you like? (espresso/latte/cappuccino):")
    choice=input().lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${money}")
    elif choice=="refill":
        water=int(input("How much amount of water is to be added?:"))
        resources["water"]+=water
        milk=int(input("How much amount of milk is to be added?:"))
        resources["milk"]+=milk
        coffee=int(input("How much amount of coffee is to be added?:"))
        resources["coffee"]+=coffee    
    else:
        drink=MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment=process_coins()
            transaction_completed(payment,drink['cost'])
            making_coffee(choice,drink["ingredients"])