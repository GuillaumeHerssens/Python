import re
name = input("What is your name ?")

if not name or re.fullmatch(" {1,}", name):
    name = "world"

print("Hello, %s" % (name))