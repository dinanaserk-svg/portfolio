class ClothingItem:
    def __init__(self,name,category,color,season,occasion="casual"):
        self.name=name
        self.category=category
        self.season=season
        self.occasion=occasion
        self.color=color
    def display_clothing_item_info(self):
        print("name",self.name)
        print("category",self.category)
        print("season",self.season)
        print("occasion",self.occasion)
        print("color",self.color)

class User:
    def __init__(self,name,email,age,favorite_color,favorite_season,wardrobe):
        self.name=name
        self.email=email
        self.age=age
        self.favorite_color=favorite_color
        self.favorite_session=favorite_season
        self.wardrobe=wardrobe
    def display_user_info(self):
        print("user profile")
        print("name",self.name)
        print("email",self.email)
        print("age",self.age)
        print("favorite_color",self.favorite_color)
        print("favorite_session",self.favorite_session)

