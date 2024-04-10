import random

inventory = ["Bandage Bundle", "Sack of Equipments"]
health = 15
gold = 150
energylvl = 47

def mine():
    global health
    
    chance = random.randint(1, 100)
    quantityperc = random.randint(1, 100)

    oreamount = 0
    
    if quantityperc < 30:
        oreamount = 1
    elif quantityperc >= 30 and chance < 55:
        oreamount = 2
    elif quantityperc >= 55 and chance < 75:
        oreamount = 3
    elif quantityperc >= 75 and chance < 90:
        oreamount = 4
    elif quantityperc >= 90 and chance < 97:
        oreamount = 5
    elif quantityperc >= 97 and chance < 100:
        oreamount = 10
        
    if chance < 15:
        ore = None
    elif chance >= 15 and chance < 40:
        ore = "Limestone"
    elif chance >= 40 and chance < 60:
        ore = "Platinum"
    elif chance >= 60 and chance < 75:
        ore = "Silver"
        addinv(ore, oreamount)
    elif chance >= 75 and chance < 85:
        ore = "Luminite"
    elif chance >= 85 and chance < 95:
        ore = "Gold"
    elif chance >= 95 and chance <= 100:
        ore = "Wrathmetal"
        
    if ore == "Wrathmetal":
        health -= random.randint(10, 25)

    if ore != None and oreamount != 0:
        print("Your mining session was succesful. Here is your new inventory:", inventory)
        addinv(ore, oreamount)
    else:
        print("You couldn't find any ores, that's very sad.")

def addinv(item, quantity):
    if isinstance(quantity, int) and isinstance(item, str):
        if quantity == 0:
            inventory.append(item)
        else:
            found_vessel = False
            for i, itemval in enumerate(inventory):
                if ":" in item:
                    item_name, amount = itemval.split(":")
                    item_name = item_name.strip()
                    amount = str(amount)
                    amount = amount.strip()
                    if item_name == item:
                        amount = int(amount)
                        amount += quantity
                        newval = item_name + ": " + str(amount)
                        
                        found_vessel = True
                        break
                    else:
                        continue
                else:
                    continue
            if found_vessel is False:
                inventory.append(item + ": " + str(quantity))
    else:
        print("Invalid Argument: Quantity must be integer | Item must be a string")
def removeinv(item, quantity):
    if isinstance(quantity, int) and isinstance(item, str):
        if quantity == 0:  # Change to handle removing entire item
            inventory.remove(item)
        else:
            if item not in inventory:
                print("No item to remove.")
            else:
                for i, itemval in enumerate(inventory):
                    if ":" in itemval:
                        invitem, amount = itemval.split(":")
                        if item == invitem:
                            amount = int(amount.strip())
                            amount -= quantity
                            if amount <= 0:
                                inventory.pop(i)
                            else:
                                completeitem = item + ": " + str(amount)
                                inventory[i] = completeitem
                            break
                else:
                    print("Item not found in inventory.")
    else:
        raise ValueError("Invalid Argument: Quantity must be integer | Item must be a string")

def use(item):
    global health
    global energylvl
    
    if item == "Bandage Bundle":
        removeinv("Bandage Bundle", 0)
        addinv("First Aid Kit", 0)
        addinv("Bandages", 5)
        print("You opened the bundle, it had a First aid kit and some Bandages")
        
    elif item == "Sack of Equipments":
        removeinv("Sack of Equipments", 0)
        addinv("Pickaxe", 0)
        addinv("Axe", 0)
        addinv("Food", 3)
        print("You open your sack. It has a pickaxe, an axe, and food")
        
    elif item == "First Aid Kit":
        removeinv("First Aid Kit", 0)
        health += 75
        print("You treated yourself and healed by 75 points:", health)

    elif item == "Bandages":
        removeinv("Bandages", 1)
        health += 20
        print("You treated yourself and healed by 20 points:", health)
        
    elif item == "Food":
        energylvl += 15
        print("You eat food and gain 15 points of energy")

while True:
    print("You've recently decided to explore the world, you've got some of your stuff in bundles: A pack of bandages and some useful equipment")
    print("Recently you've been attacked by some slavers, and narrowly escaped.")
    playercall = input("""You need to heal. Unpack your bandages and use one.
Use Items [1]
Skip Tutorial [2]
Input "1" to go to the item menu and use them: """)
    if playercall == "1":
        print("""You look in your inventory, what will you use?""")
        for index, value in enumerate(inventory):
            print(value, "[" + str(index) + "]")
        playercall = input("Select a number: ")
        chosen_index = int(playercall)  # Convert input to integer
        if chosen_index < len(inventory):  # Ensure chosen index is within range
            if chosen_index == 0:
                use(inventory[chosen_index])
                break
            else:
                print("That is the wrong item!")
        else:
            print("Invalid selection.")
            
    elif playercall == "2":
        print("Skipping Tutorial...")
        health += 75
        addinv("Bandages", 5)
        addinv("Pickaxe", 0)
        addinv("Axe", 0)
        addinv("Food", 3)
        removeinv("Bandage Bundle", 0)
        removeinv("Sack of Equipments", 0)
        break
        
    else:
        print("This is not a valid action")

while "First Aid Kit" in inventory or "Sack of Equipments" in inventory:
    print("Now that you've opened the sack, you need to use the kit. Then, open up the sack of equipments")
    playercall = input("""You need to heal.
Use Items [1]
Input "1" to go to the item menu and use them: """)
    if playercall == "1":
        print("""You look in your inventory, what will you use?""")
        for index, value in enumerate(inventory):
            print(value, "[" + str(index) + "]")
        playercall = input("Select a number: ")
        chosen_index = int(playercall)
        if chosen_index < len(inventory):
            use(inventory[chosen_index])
        else:
            print("Invalid selection.")

print("WARNING - This is the most of a tutorial you'll get! Learn the game yourself")

while True:
    action = input("""What action will you make?
    Mine [1]
    Woodchop [2]
    Shop [3]
    Use Items [4]
    Exploration [5]
    Craft [6]
    What will you do now: """)
    if action == "1":
        mine()
    elif action == "2":
        print("placeholder")
    elif action == "3":
        print("placeholder")
    elif action == "4":
        print("placeholder")
    elif action == "5":
        print("placeholder")
    elif action == "6":
        print("placeholder")
    else:
        print("That's not a choice!")
























