
import sys
import time
from datetime import datetime
from os import getcwd

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
	21, 23, 25, 27, 29, 31, 33, 25, 37, 39,
	41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute
where_am_i = getcwd()
now = time.strftime("%A:%p")

print(where_am_i)
print(now)
print(" ")
print(" ")

import sys

if right_this_minute in odds:
	print("this minute seems a little odd.")
else:
	print("Not an odd minute.")

