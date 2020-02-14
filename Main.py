# Zane M Torregrossa
# This is Adventuria! A fun and diverse dungeon exploring game.
# Can you make it to the end alive?


# Starting Adventure
def start_adventure():
    print("You awake in a cold and dark room.")
    print("You see a red door on the right and a blue door to your left.")
    main_room()


# Creating a Beginning Room
def main_room():
    print("It seems you cannot see anything else in this room.")
    print("Do you pick the red door or the blue door?")
    main_room_doors = input(">")
    if main_room_doors in ["red door", "red", "right"]:
        print("You chose the red door. You begin to open the door...")
        red_door_room()
    elif main_room_doors in ["blue door", "blue", "left"]:
        print("You chose the blue door. You begin to open the door...")
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer.")
        main_room()


# Setting up Red Door Room
def red_door_room():
    print("You enter the room behind the red door.")
    print("In the room, you see a great, giant, red dragon sleeping in the middle of the floor.")
    print("There is an Orange Door behind the beast.")
    action_step4()


# Setting up Blue Door Room
def blue_door_room():
    print("You enter the room behind the blue door.")
    print("You glance around the room.")
    print("You can see a wooden chest on the left, a sleeping guard on the right, and a yellow door in the middle.")
    action_step1()


# Setting up Yellow Door Room
def yellow_door_room():
    print("After unlocking the old, ancient door, you push it wide open; entering a room full of darkness.")
    print("There seems to be torches along the wall. Perhaps one can be sparked for a source of light?")
    print("Do you want to light a torch?")
    choice_step3()


# Setting up Action Commands
def action_step1():
    print("What do you want to do?")
    act_step1 = input(">")
    if act_step1 in ["wooden chest", "wooden", "chest", "left"]:
        print("You reach for the wooden chest. Are you sure you want to open it?")
        choice_step1()
    elif act_step1 in ["yellow", "middle", "door"]:
        print("You jiggle the door handle, but it won't open!")
        action_step2()
    elif act_step1 in ["guard", "right"]:
        print("You turn to face the guard.")
        action_step3()
    else:
        print("Sorry, it's either 'chest', 'yellow', or 'guard' as the answer.")
        blue_door_room()


def action_step2():
    print("Do you want to check the guard, the yellow door, or go back to previous room?")
    act_step2 = input(">")
    if act_step2 in ["go back", "previous room"]:
        main_room()
    elif act_step2 in ["yellow", "middle", "door"]:
        print("You jiggle the door handle, but it won't open!")
        blue_door_room()
    elif act_step2 in ["guard", "right"]:
        print("You turn to face the guard.")
        action_step3()
    else:
        print("Sorry, your choices are 'go back', 'yellow', or 'guard'.")
        blue_door_room()


def action_step3():
    print("The guard is still sleeping. Would you like to pickpocket, fight, or leave him be?")
    act_step3 = input(">")
    if act_step3 == "pickpocket":
        print("You begin going through his pockets...")
        print("You find a key with a skull on it.")
        action_step2()
    elif act_step3 == "fight":
        print("You go to attack the guard, but he awakens and swiftly dodges your attack!")
        action_step5()
    elif act_step3 == "leave":
        print("Well okay then, let the man sleep in peace.")
        action_step2()
    else:
        print("Sorry, your choices are 'pickpocket', 'fight', or 'leave'.")
        blue_door_room()


def action_step4():
    print("Do you Go Back, Fight the dragon, or Sneak past the dragon?")
    act_step4 = input(">")
    if act_step4 in ["Go Back", "Back", "go back", "back"]:
        print("You turn around and go back the way you came.")
        main_room()
    elif act_step4 in ["Fight", "fight", "Fight the dragon", "fight the dragon"]:
        print("You attack the dragon.")
        print("The dragon awakes and eats you whole. Well, that was tasty!")
        game_over()
    elif act_step4 in ["Sneak", "sneak", "Sneak past the dragon", "sneak past the dragon"]:
        print("You begin to quietly walk past the dragon.")
        print("As you approach the other side of the room, you can see the Orange Door is covered in dust.")
        print("Do you want to clean the door?")
        choice_step4()
    else:
        print("Sorry, it's either 'go back', 'fight' or 'sneak' as the answer.")
        red_door_room()


def action_step5():
    print("")
    act_step5 = input(">")
    if act_step5 in [""]:
        print("")

    elif act_step5 in [""]:
        print("")

    else:
        print("Sorry, your choices are '' or ''.")


# Setting up Choice Commands
def choice_step1():
    treasure_chest = ["3 Sparkling Diamonds, 10 Shiny Gold Coins, 25 Silver Septums, and an Old Sword."]
    choice1 = input(">")
    if choice1 == "yes":
        print("Let's see what's in here...")
        print("The chest creaks open. You can hear the guard is still sleeping. That's one heavy sleeper!")
        print("Inside the chest, you find:")
        for treasure in range(len(treasure_chest)):
            print(treasure_chest[treasure])
            print("There is a warning inside the chest!")
            print("Adventurer, this is a magical chest. You get one item, the rest will disappear! Choose carefully...")
            print("Which item will you take?")
            choice_step2()
    elif choice1 == "no":
        print("Oh okay, no loot for you.")
        action_step2()
    else:
        print("Sorry, your choices are 'yes' or 'no'.")
        blue_door_room()


def choice_step2():
    choice2 = input(">")
    if choice2 in ["sparkling diamonds", "Sparkling Diamonds", "diamonds", "Diamonds"]:
        print("You chose the Sparkling Diamonds. Oh how they sparkle!")
        action_step2()
    elif choice2 in ["Shiny Gold", "shiny gold", "Gold", "gold"]:
        print("You chose the Shiny Gold. Is there ever enough wealth?")
        action_step2()
    elif choice2 in ["Silver Septums", "Silver", "silver septums", "silver"]:
        print("You chose Silver. What are you? Stupid or something?")
        action_step2()
    elif choice2 in ["Old Sword", "old sword", "Sword", "sword"]:
        print("You chose the Old Sword. Ah, what a fine weapon you have there!")
        action_step2()
    else:
        print("Sorry, your choices are 'Diamonds', 'Gold', 'Silver', or 'Sword'.")
        choice_step1()


def choice_step3():
    choice3 = input(">")
    if choice3 == "yes":
        print("The torch lights. A light is now provided.")
    elif choice3 == "no":
        print("You fool, how will you see in this darkness?")
    else:
        print("Sorry, your choices are 'yes' or 'no'.")
        yellow_door_room()


def choice_step4():
    choice4 = input(">")
    if choice4 == "yes":
        print("You wipe the dust off the door. A symbol of a Skull appears on the door.")
        # Need to create a way to identify if user has key
    elif choice4 == "no":
        print("That must say something about your cleanliness!")
        # Figure out what happens next
    else:
        print("Sorry, your choices are 'yes' or 'no'.")
        action_step4()


# Setting up Player and Game Start
def main():
    player_name = input("What is your name, Adventurer? >")
    print("Your name is {}.".format(player_name))
    start_adventure()


# Reset or Quit the Game
def game_over():
    reset_game = input("Game Over, Adventurer. Try again? 'yes' or 'no' >")
    if "yes" in reset_game:
        start_adventure()
    elif "no" in reset_game:
        print("Pity. We thought you were the Chosen One.")
        quit()


if __name__ == '__main__':
    main()
