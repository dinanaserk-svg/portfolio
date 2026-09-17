import json

class Wardrobe:
    def __init__(self):
        self.clothes_list = []
        try:
            with open("wardrobe.json", "r") as file:
                self.clothes_list = json.load(file)
        except:
            self.clothes_list = []

    def save(self):
        with open("wardrobe.json", "w") as file:
            json.dump(self.clothes_list, file)

    def add_item(self, item):
        cloth_data = {
            "name": item.name,
            "category": item.category,
            "color": item.color,
            "season": item.season,
        }
        self.clothes_list.append(cloth_data)
        self.save()
        print("Item added successfully!")

    def remove_item(self, name):
        for item in self.clothes_list:
            if item["name"] == name:
                self.clothes_list.remove(item)
                self.save()
                print("Item removed successfully!")
                return
        print("Item not found!")

    def filter_by(self, key, value):
        results = []
        for item in self.clothes_list:
            if item.get(key) == value:
                results.append(item)
        return results

    def display_items(self):
        print("Wardrobe Items:", self.clothes_list)

        
