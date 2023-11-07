class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self):
        print(self.name + " doesn't want to fight with you")
        return True
class Enemy(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness = None
        self.items = None
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            print(f"You loot {self.items} from {self.name}")
            return True,self.items
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    def set_items(self,items):
        self.items = items
    def set_weakness(self,weakness):
        self.weakness = weakness
    def steal(self):
        if self.items is not None:
            for i in range(len(self.items)):
                print(f"You steal {self.items[i]} from {self.name}")
            item = self.items
            self.items = None
            return item
        else:
            print("there is nothing to steal")
            return None
class Friend(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)