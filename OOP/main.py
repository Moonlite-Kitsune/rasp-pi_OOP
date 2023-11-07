from room import Room
from character import Enemy,Friend
def init_map():
    kitchen = Room("kitchen")
    kitchen.set_description("A dank and dirty room buzzing with flies")
    dining_hall = Room("dining hall")
    dining_hall.set_description("A large room with ornate golden decorations on each wall")
    ballroom = Room("ballroom")
    ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
    dining_hall.link_room(ballroom,"West")
    ballroom.link_room(dining_hall,"East")
    dining_hall.link_room(kitchen,"North")
    kitchen.link_room(dining_hall,"South")
    dave = Enemy("Dave","A smelly zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("cheese")
    dave.set_items(["1gp"])
    catrina = Friend("Catrina", "A friendly skeleton")
    catrina.set_conversation("Why hello there")
    ballroom.set_character(catrina)
    dining_hall.set_character(dave)
    current_room = kitchen
    gp = 0
    inventory=[]
    alive = True
    return alive,current_room,gp,inventory
alive,current_room,gp,inventory = init_map()         
while alive:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()  
    print("commands:North, South, East, West, Steal, Inventory, Gold")       
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
                if inhabitant.fight(fight_with)[0] == True:
                    alive = True
                    if inhabitant.fight(fight_with)[1] is not None:
                        for i in inhabitant.fight(fight_with)[1]:
                            inventory.append(i)
                    current_room.set_character(None)
                else:
                    alive = False
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
print("Game Over")