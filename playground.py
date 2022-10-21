import json

fav_num = int(input("what is your favorite number? "))
with open("play.json", "w") as f:
    json.dump(f"{fav_num}", f)

with open("play.json") as f:
    list = json.load(f)

    print(list)
