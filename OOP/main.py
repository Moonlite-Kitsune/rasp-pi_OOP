from room import Room
from item import Item
from character import Enemy,Friend
from rpginfo import RPGInfo
spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
def init_map():
    kitchen = Room("kitchen")
    kitchen.set_description("A dank and dirty room buzzing with flies")
    dining_hall = Room("dining hall")
    dining_hall.set_description("A large room with ornate golden decorations on each wall")
    ballroom = Room("ballroom")
    ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
    exit = Room(exit)
    exit.set_description("Alarge ornate door with a hole in the centre")
    dining_hall.link_room(ballroom,"West")
    ballroom.link_room(dining_hall,"East")
    dining_hall.link_room(kitchen,"North")
    kitchen.link_room(dining_hall,"South")
    ballroom.link_room(exit,"North")
    exit.link_room(ballroom,"South")
    print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
    dave = Enemy("Dave","A smelly zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("cheese")
    dave.set_items(["1gp","artifact"])
    catrina = Friend("Catrina", "A friendly skeleton")
    cheese = Item("Cheese")
    Item.set_description("a hard block of cheese")
    catrina.set_conversation("Why hello there")
    ballroom.set_character(catrina)
    dining_hall.set_character(dave)
    kitchen.set_item(cheese)
    current_room = kitchen
    gp = 0
    inventory=[]
    return alive,current_room,gp,inventory
alive,current_room,gp,inventory = init_map()         
while True:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()  
    print("commands:North, South, East, West, Steal, Inventory, Gold, Search, Interact")       
    command = input("> ").capitalize()
    if command in ["North","South","East","West"]:  
        current_room = current_room.move(command) 
    elif command == "Talk":
        inhabitant.talk()
    elif command == "Fight":
        if inhabitant is not None:
            if not isinstance(inhabitant,Friend):
                print("what will you fight with?")
                fight_with = input("> ")
                if fight_with in inventory:
                    if inhabitant.fight(fight_with) == True:
                        if inhabitant.fight(fight_with)[1] is not None:
                            for i in inhabitant.fight(fight_with)[1]:
                                inventory.append(i)
                        current_room.set_character(None)
                    else:
                        print("Game Over, you died")
                        break
                else:
                    print("you don't have that item")
            else:
                print("that is a friend")
    elif command == "Steal":
            if inhabitant is not None:
                if not isinstance(inhabitant,Friend):
                    stolen = inhabitant.steal()
                    if stolen is not None:
                        for i in stolen:
                            inventory.append(i)
                else:
                    print("that is a friend")
            else:
                print("there is no one to steal from")
    elif command == "Inventory":
        if inventory != []:
            print("you have:",end =" ")
            for i in inventory:
                print(i,end=",")
        else:
            print("you have nothing")
    elif command == "Gold":
        print(f"gold: {gp}")
    if inventory != []:
        for i in range(len(inventory)):
            if inventory[i][-2:len(inventory[i])] == "gp":
                gp += int(inventory[i][0:-2])
                inventory.remove(inventory[i])
    elif command == "Interact":
        if current_room == exit:
            if "artfact" in inventory:
                print("You place the item in the hole in the door and it swings open")
                print("Game Over, you escaped")
                break
            else:
                print("you do not have the required item")
        else:
            print("there is nothing to interact with")
    elif command == "Search":
        if current_room.item is not None:
            print(f"you find a(n) {current_room.item}")
            inventory.push(current_room.item)
            current_room.item = None
        else:
            print("there is nothing in the room")
RPGInfo.author = "Moonlite_Kitsune"
RPGInfo.co_author = "Raspberry Pi Foundation"
RPGInfo.credits()