class Room:
    number_of_rooms = 0
    def __init__(self, roomName):
        self.name = roomName
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        Room.number_of_rooms +=1
    def get_description(self):
        return self.description
    def get_name(self):
        return self.name
    def set_character(self,character):
        self.character = character
    def get_character(self):
        return self.character
    def set_item(self, item):
        self.item = item
    def get_item(self):
        return self.item
    def set_description(self, room_description):
        self.description = room_description
    def describe(self):
        print( self.description )
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self