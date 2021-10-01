import re
from morse_dict import morse_dict

class Translate:
    def __init__(self, alpha_input):
        self.alpha_input = alpha_input
        self.morse_dict = morse_dict

    def print_morse(self):
        morse_code_output = ""

        for letter in self.alpha_input:
            morse_code_output += self.morse_dict[letter]

        return(f"\n{morse_code_output}\n")

translate = Translate("a")
translate.print_morse()