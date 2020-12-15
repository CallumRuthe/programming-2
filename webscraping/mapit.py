# mapit.py - tool to search physical addresses
# usage -- python mapit.py 6600 Williams Road Richmond
#     output: should take us to the address in GMaps

import webbrowser
import sys
import pyperclip


# If there are no ARGUMENTS
# grab address from the clipboard
if len(sys.argv) < 2:
    address = pyperclip.paste()

else:
    address = " ".join(sys.argv[1:])
    # join(list) --> takes list and combines into a string seperated by " "

print(f"Finding {address}")
prefix = "https://google.com/maps/place/"
webbrowser.open(prefix+address)
