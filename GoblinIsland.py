print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("The world is vast, the treasures many, and the dangers even greater. Step forward, and your story begins. Welcome to Goblin Island.")
print("Legends speak of a goblin’s treasure hidden somewhere in the area. Your task: claim it… and live to tell the tale.")

first_move = input("You find yourself at a crossroads. Which way would you like to go? Type \"left\" or \"right\"\n")
if first_move == "left" or first_move == "Left":
    second_move = input("After an hour of walking across a neat cobblestone road, you stumble upon a big red lake. "
          "There is an fog-covered island in the middle of the lake. "
          "Type \"wait\" to wait for the ferry. Type \"swim\" to try and swim across.\n")

    if second_move == "wait" or second_move == "Wait":
        third_move = (input("The ferryman greets you warmly and launches into a long tale about his wife and son, filling the air with stories as the boat drifts across the water. "
                            "Eventually, you reach the island unharmed. "
                            "You hand the ferryman a single copper coin, step off the ferry, and wander toward the island. He’s still talking, oblivious to your departure. Rude, but effective. "
                            "After a short while, the fog clears and you find yourself facing a house with 3 doors. "
              "One \"red\", one \"green\", and one \"blue\". Which color do you choose?\n"))
        if third_move == "red" or third_move == "Red":
            print("You touch the iron handle to the red door, and before you can even blink, you hear the sound of heavy, guttural breathing behind you, and you feel a searing white pain shooting through your neck. "
                  "The goblin has found you, and now, you have no head. You are dead.")
        elif third_move == "green" or third_move == "Green":
            print("You turn the brass handle on the green door and are instantly met with the comforting scent of fresh honey, cold ale, and meat bubbling on the stove. "
                  "The warmth of the room wraps around you like a blanket. "
                  "Before you stands an elderly goblin woman, smiling from ear to ear. "
                  "\"Oh, happy days! A visitor at last!\" she exclaims. \"Please, come in, have a seat, my dear. I haven’t had anyone to talk to in decades!\" "
                  "You open your mouth to protest… then close it again. Refusing her would make you a terrible person. "
                  "And so, you sit. "
                  "And you listen. "
                  "Forever. "
                  "The End.")
        elif third_move == "blue" or third_move == "Blue":
            print("You push open the blue door, and a flash of blinding light floods your vision. "
                  "As your eyes adjust, you see a massive treasure chest overflowing with gold and glittering jewels. "
                  "The room sparkles with wealth beyond imagination. "
                  "In the corner, you notice the silent remains of a few fallen adventurers, their heads missing. "
                  "Best not to dwell on that. This treasure is yours now. You win!")
        else:
            print("You stare at the door, unable—or unwilling—to choose. Hours pass. Days. Centuries. "
                  "Civilizations rise and fall around you, empires crumble, stars explode. "
                  "And still… you do not pick a color. Eventually, time itself forgets you exist. "
                  "Congratulations, you are dead… of indecision.")
    else:
        print("You decide to take a deep breath and leap into the lake, determined to swim across. "
              "Bad idea. "
              "From below rises a gigantic trout, clearly powered by dark magic and bad intentions. It stares at you for half a second. "
              "Then it eats you. "
              "Regret is brief. "
              "The End.")
else:
    print("You trip over an uneven dirt path, fall into a conveniently placed hole, and… congratulations, you are dead.")