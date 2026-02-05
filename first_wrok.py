name = input("please submit your name: ")
print("Hello there "+name)

age = int(input("and your age is: "))

while age <0 :
    print("your age cannot be negative. again: ")
    age = int(input("\nyour age: "))

while age >110 :
    print("you're not that old c mon... again: ")
    age = int(input("\nyour age: "))

if age % 2 == 0:
    print("ah, it's an even number :)")
else : print("your age is so.. odd :o")

print("\nlet us count to your age! count with me:\n ")
print(*range(age+1), sep="-")

print("\nNice! that is your age~")