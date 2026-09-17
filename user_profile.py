import json
import os

class User:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.email = ""
        self.fav_color = ""
        self.fav_season = ""

    def load_user(self):
        if os.path.exists("user_profile.json"):
            file = open("user_profile.json", "r")
            data = json.load(file)
            file.close()

            self.name = data["name"]
            self.age = data["age"]
            self.email = data["email"]
            self.fav_color = data["fav_color"]
            self.fav_season = data["fav_season"]
            return True
        else:
            return False

    def create_user(self):
        print("Welcome! Create your account:")
        self.name = input("Enter your name: ").strip()
        self.age = input("Enter your age: ").strip()
        self.email = input("Enter your email: ").strip()
        self.fav_color = input("Enter your favorite color: ").lower().strip()
        self.fav_season = input("Enter your favorite season: ").lower().strip()

        data = {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "fav_color": self.fav_color,
            "fav_season": self.fav_season,
        }

        file = open("user_profile.json", "w")
        json.dump(data, file)
        file.close()
        print("Account created successfully!")