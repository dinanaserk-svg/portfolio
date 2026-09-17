from color_rules import COLOR_RULES
class ColorMatcher:

    def __init__(self):
        self.colors_dict = COLOR_RULES

    def is_match(self, color1, color2):
        c1 = color1.lower().strip()
        c2 = color2.lower().strip()

        if c1 == c2:
            return True

        if c1 in self.colors_dict and c2 in self.colors_dict[c1]:
            return True

        if c2 in self.colors_dict and c1 in self.colors_dict[c2]:
            return True
        else:

            return False

    def suggest_outfit(self, wardrobe_list, current_season):
        tops = []
        bottoms = []
        shoes_list = []

        for item in wardrobe_list:
            item_category = item['category'].lower().strip()
            item_season = item['season'].lower().strip()
            season_now = current_season.lower().strip()

            if item_season == season_now:
                if item_category == "top":
                    tops.append(item)
                elif item_category == "bottom":
                    bottoms.append(item)
                elif item_category == "shoes":
                    shoes_list.append(item)

        for top in tops:
            for bottom in bottoms:
                for shoes in shoes_list:
                    if self.is_match(top['color'], bottom['color']) and self.is_match(bottom['color'], shoes['color']):
                        return Outfit(top, bottom, shoes)

        return None


class Outfit:
    def __init__(self, top, bottom, shoes):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes

    def print_outfit(self):
        print("Today Outfit:")
        print("Top Name:", self.top['name'])
        print("Top Color:", self.top['color'])
        print("Bottom Name:", self.bottom['name'])
        print("Bottom Color:", self.bottom['color'])
        print("Shoes Name:", self.shoes['name'])
        print("Shoes Color:", self.shoes['color'])