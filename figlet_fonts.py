from pyfiglet import Figlet
import random
import sys
import pyttsx3


figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(text))


elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    pass


else:
    sys.exit("Invalid usage")
