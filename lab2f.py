#!/usr/bin/env python3

# Author: [Urmil Rohitkumar Patel]
# Author ID: [153090220]
# Date Created: 2025/01/31

import sys

# Assign the value from the command line argument to the timer
timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
