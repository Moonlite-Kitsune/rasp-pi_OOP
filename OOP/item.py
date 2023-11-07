class Item:
    def __init__(self,itemName):
        self.Name = itemName
        self.description = None
    def get_name(self):
        return self.Name
    def set_description(self,description):
        self.description = description
    def get_description(self):
        return self.description