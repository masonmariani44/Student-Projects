import time

age = int(input("Enter your age: "))
name = input("Enter your name: ")

print("My name is " + name + " my age is " + str(age))


time.sleep(3)

if age < 18:
    print("You are a kid")
elif age < 35:
    print("You are a young adult")
elif age < 65:
    print("Youre just an adult.")
elif age > 65:
    print("You are a senior citizen.")


def walk(distance):
    position += distance
    print("operation complete")
    return True

walk(5)