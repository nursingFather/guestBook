from remember_me import UserVerifier
from favno import FavouriteNumber

user_verifier = UserVerifier()
lucky_number = FavouriteNumber()

#confiriming user identity
current_user = user_verifier.remember_user()
print(f"Is '{current_user}' your correct username?")
verification = input("press 'y' for YES and 'n' for NO... ")

#reading favorite number
number = lucky_number.read_number()

if verification == "y":
    greetings = user_verifier.greet_user()
    print(greetings)
elif verification == "n":
    current_user = user_verifier.create_username()
    greetings = user_verifier.greet_new_user()
    print(greetings)

if verification != "y" or "n":
    print("please enter the correct command")
else:
    print(f"{current_user}, your favorite number is {number}")