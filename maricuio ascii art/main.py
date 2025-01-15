def main(width, height):

    print("-" * width)

    for i in range(height):
        print("|" + " " * (width - 2) + "|")
    
    print("-" * width)


#main(50, 35)

"""
-------
|     |
|     |
|     |
-------
"""

"""
Animal: Cat Says: meow
Animal: Dog Says: woof
Animal: Elephant Says: BBRRTTTT!!!
"""

def string_func(animal, sound):
    test_string = f"Animal: {animal} Says: {sound}"

    print(test_string)





animal_sounds = {

    "dog" : "woof",
    "cat" : "meow",
    "bird" : "chirp"

}

for item in animal_sounds:
    string_func(item)