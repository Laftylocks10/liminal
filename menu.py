mango_amount = 20
watermelon_amount = 10
apple_amount = 30
orange_amount = 40
mango_cost = 1.0
watermelon_cost = 10.0
apple_cost = 1.0
orange_cost = 0.5
player_money = 100.0
afford = bool
buy_amount = 0

def buy(item_cost):
    global player_money
    global afford
    
    if player_money >= item_cost:
        player_money -= item_cost
        print(f"That'll be ${item_cost}¢, thank you!")
        print(f"Your networth has been decreased to ${player_money}¢")
        afford = True
    else:
        print("You cannot afford that!")
        afford = False

print("Welcome to Tim's Store of Fruits and Veggies!")
while player_money >= 5.0:
    print(f"""What would you like to order?
 [1] Mango - {mango_amount} - ${mango_cost}¢
 [2] Watermelon - {watermelon_amount} - ${watermelon_cost}¢
 [3] Orange - {orange_amount} - ${orange_cost}¢
 [4] Apple - {apple_amount} - ${apple_cost}¢""")
    print(f"You have ${player_money}¢")
    decision = str(input("Which would you like to buy: "))
    if decision in ["1", "2", "3", "4"]:
        if decision == "1":
            buy_amount = int(input("How many would you like to buy: "))
            if mango_amount == "Out of Stock!" or mango_amount < buy_amount:
                print("I'm sorry, but we don't have enough mangoes")
            else:
                buy(mango_cost*buy_amount)
                if afford == False:
                    continue
                mango_amount -= buy_amount
                if mango_amount == 0:
                    mango_amount = "Out of Stock!"
                print(f"You bought {buy_amount} mango")
        if decision == "2":
            buy_amount = int(input("How many would you like to buy: "))
            if watermelon_amount == "Out of Stock!" or watermelon_amount < buy_amount:
                print("I'm sorry, but we don't have enough watermelons")
            else:
                buy(watermelon_cost*buy_amount)
                if afford == False:
                    continue
                watermelon_amount -= buy_amount
                if watermelon_amount == 0:
                    watermelon_amount = "Out of Stock!"
                print(f"You bought {buy_amount} watermelon")
        if decision == "3":
            buy_amount = int(input("How many would you like to buy: "))
            if orange_amount == "Out of Stock!" or orange_amount < buy_amount:
                print("I'm sorry, but we don't have enough oranges")
            else:
                buy(orange_cost*buy_amount)
                if afford == False:
                    continue
                orange_amount -= buy_amount
                if orange_amount == 0:
                    orange_amount = "Out of Stock!"
                print(f"You bought {buy_amount} orange")
        if decision == "4":
            buy_amount = int(input("How many would you like to buy: "))
            if apple_amount == "Out of Stock!" or apple_amount < buy_amount:
                print("I'm sorry, but we don't have enough apples")
            else:
                buy(apple_cost*buy_amount)
                if not afford:
                    continue
                apple_amount -= buy_amount
                if apple_amount == 0:
                    apple_amount = "Out of Stock!"
                print(f"You bought {buy_amount} apple")
print("You went broke and became homeless")
