class RPGInfo:
    author = "Anonymous"
    co_author = "Anonymous"
    def __init__(self,game_title):
        self.title = game_title
    def welcome(self):
        print(f"Welcome to {self.title}")
    @staticmethod
    def info():
        print("Made uding the OOP RPG game creator (c)")
    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"Created by {cls.author}")
        print(f"co-authored by {cls.co_author}")