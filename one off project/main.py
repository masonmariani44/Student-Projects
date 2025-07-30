import random

jokes_list = ["joke1",
              "joke2",
              "joke3"]

while True:

    user_input = input("give me input")

    if user_input == "tell me a joke":
        random_number = random.randint(0, len(jokes_list) - 1)
        print(jokes_list[random_number])







































import random


jokes_list = [
    "Have you heard of that new band \"1023 Megabytes\"?... They're pretty good, but they don't have a gig just yet.",
    "What did the computer have during his break time?... He had a byte!",
    "Why did the developer become so poor?... Because he cleared his cache.",
    "Why are Microsoft employees never relaxed?... Because they're always on Edge.",
    "How many programmers does it take to change a light bulb?... None, because it is a hardware problem.",
    "hilarious joke"
]


isRunning = True
while isRunning:
    user_input = input("Give me input: ")

    if user_input == "hello":
        print("hi im a computer")
    if user_input == "how are you":
        print("doing good")
    if user_input == "what are your specs":
        print("pretty good")
    if user_input == "tell me a joke":
        rand = random.randint(0, len(jokes_list)-1)
        print(jokes_list[rand])
    if user_input == "goodbye":
        print("see ya!")
        isRunning = False

