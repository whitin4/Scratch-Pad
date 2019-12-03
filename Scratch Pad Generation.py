from datetime import datetime
import os

print("New note:")
note = [input()]
print(note)

# Today's date, yyyy-mm-dd
now = datetime.now().strftime("%y%m%d%H%M%S")
filename = "/" + now + ".txt"

# The filepath, including file name
filepath = "C:/Users/Owner/Desktop" + filename


file = open(filepath, "w")
file.writelines(note)
file.close()
