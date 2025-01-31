#!/usr/bin/env python3

# Author: [Urmil Rohitkumar Patel]
# Author ID: [153090220]
# Date Created: 2025/01/31

import sys

# Check if an argument is provided
if len(sys.argv) > 1:
    # If an argument is provided, use it for the timer
    timer = int(sys.argv[1])
else:
    # If no argument is provided, set the timer to 3
    timer = 3

# Countdown while the timer is greater than 0
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
