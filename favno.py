import json

FILENAME = "fave_no.json"

class FavouriteNumber:
    def __init__(self):
        """initialize the attribute of the class"""

    def get_favorite_number(self):
        """get and store user favorite number"""
        try:
            self.fav_num = int(input("what is your favorite number? "))
        except ValueError:
            print("please enter a digit, not letter")
        else:
            with open(FILENAME, "w") as f:
                json.dump(self.fav_num, f)
            return self.fav_num

    def read_number(self):
        """read stored json and """
        try:
            with open(FILENAME) as g:
                self.fav_num = json.load(g)
        except FileNotFoundError:
            return self.get_favorite_number()
        else:
            return self.fav_num

    # number = read_number()
    # if number:
    #     print(f"i know your favorite number and it is {number}")
    # else:
    #     get_favorite_number()
    #     print(f"now i know it.. it is {number}")
