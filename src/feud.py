import json, urllib.request, requests

answer = "news"

with urllib.request.urlopen("https://www.reddit.com/r/" + answer + "/.json") as file:
    data = json.load(file)

max_guesses = 5
for i in range(max_guesses):
    print(data["data"]["children"][i]["data"]["title"])
    guess = input("Guess: ")
    if guess == answer:
        print("Correct!")
        break