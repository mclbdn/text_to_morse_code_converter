import re
from flask import Flask, render_template

app = Flask(__name__)

# morse_dict = {
#     # Letters
#     "a": ".- ",
#     "b": "-... ",
#     "c": "-.-. ",
#     "d": "-.. ",
#     "e": ". ",
#     "f": "..-. ",
#     "g": "--. ",
#     "h": ".... ",
#     "i": ".. ",
#     "j": ".--- ",
#     "k": "-.- ",
#     "l": ".-.. ",
#     "m": "-- ",
#     "n": "-. ",
#     "o": "--- ",
#     "p": ".--. ",
#     "q": "--.- ",
#     "r": ".-. ",
#     "s": "... ",
#     "t": "- ",
#     "u": "..- ",
#     "v": "...- ",
#     "w": ".-- ",
#     "x": "-..- ",
#     "y": "-.-- ",
#     "z": "--.. ",
#     # Numbers
#     "1": ".---- ",
#     "2": "..--- ",
#     "3": "...-- ",
#     "4": "....- ",
#     "5": "..... ",
#     "6": "-... ",
#     "7": "--... ",
#     "8": "---.. ",
#     "9": "----. ",
#     "0": "----- ",
#     # Symbols
#     "?": "..--.. ",
#     ".": "._._._ ",
#     ",": "--..-- ",
#     # Space
#     " ": "/ "
# }


# def get_input():
#     # replace() is necessary because latter isalnum() doesn't accept spaces
#     return input("Please enter a valid text (numbers/letters/space/?/,): ").lower()


# def print_morse(alpha_input):
#     morse_code_output = ""

#     for letter in alpha_input:
#         morse_code_output += morse_dict[letter]

#     print(f"\n{morse_code_output}\n")

#     want_to_continue = input("Do you wish to translate more text? ('yes'/'no'): ").lower()

#     if want_to_continue == "yes":
#         user_input = get_input()
#         print_morse(user_input)


# while True:
#     user_input = get_input()
#     if re.match(r"^[a-zA-Z0-9 ?.,]*$", user_input):
#         print_morse(user_input)
#         break
#     else:
#         print("This is not a valid text.")
#         continue

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)