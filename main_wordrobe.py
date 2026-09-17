from color_rules import COLOR_RULES
from clothing_item_and_user import ClothingItem
from outfit import ColorMatcher
from wardrobe import Wardrobe
from Weather import Weather
from user_profile import User

my_weather = Weather()
matcher = ColorMatcher()
my_wardrobe = Wardrobe()
current_user=User()

print(" Welcome to StyleDoulabi ")
if current_user.load_user():
    print("welcome back",current_user.name)
else:current_user.create_user()

my_weather.display_info()
while True:
    print("What do you want to do?")
    print("1. Add item")
    print("2. Display wardrobe")
    print("3. Check 2 colors")
    print("4.suggest outfit")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        category = input("Enter category (Top/Bottom/shoes): ")
        color = input("Enter color: ")
        season = input("Enter season: ")
        occasion=input("enter occasion")

        item = ClothingItem(name, category, color, season,occasion)
        my_wardrobe.add_item(item)

    elif choice == "2":
        my_wardrobe.display_items()

    elif choice == "3":
        c1 = input("Enter first color: ")
        c2 = input("Enter second color: ")
        result = matcher.is_match(c1, c2)
        print("Matching result:", result)

    elif choice == "4":
        current_season = my_weather.season()
        my_outfit = matcher.suggest_outfit(my_wardrobe.clothes_list, current_season)

        if my_outfit!= None:
            my_outfit.print_outfit()
        else:
            print("No matching outfit found for this season!")
    elif choice == "5":
     print("Goodbye!")
     break

    else:
        print("Invalid choice, try again.")