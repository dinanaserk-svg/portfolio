import datetime
class Weather:
    def __init__(self):
        self.date=datetime.date.today()
        self.month=self.date.month
    def season(self):
        if self.month in [6,7,8,9]:
            return "summer"
        elif self.month in [10,11]:
            return "autumn"
        elif self.month in[12,1,2]:
            return "winter"
        else:
            return "spring"

    def temperature(self):
        current_season=self.season()
        if current_season == "summer":
            return 35
        elif current_season == "spring":
            return 22
        elif current_season == "autumn":
            return 18
        else:
            return 10

    def display_info(self):
        print("Date:", self.date)
        print("Season:", self.season())
        print("Temperature:", self.temperature(), "C")

