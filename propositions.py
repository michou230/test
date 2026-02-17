is_raining = False
is_sunny = True

print(type(is_raining))

x = 7
y = 26

print(x>y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=7)

p = True 
print(not p)

is_cold = False
print(not is_cold)

user = "admin" 
password = 12345
is_verified = True
role = "user"

if user == "admin" and password == 12345 and is_verified:
    print("Allowed.")
else : print("Not Allowed.")

if role == "admin":
    print("You have access to all features.")
else: print("You're just a user, you only have limited access.")