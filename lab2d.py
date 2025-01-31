#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Exit with code 0 when there are errors in argument count

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + age + " years old.")

