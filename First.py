import sys
print("Welcome to my first webapp")
print("whats your name?")
name = input ()
print(f"welcome {name}" )
print("how old are you?")
ixage = input()
try:
	age = int(ixage)
except Exception:
   	sys.exit("not a number")
if age < 20:
		print("Still Young")
elif age > 20:
		print("getting old")
else:
		print("error")
