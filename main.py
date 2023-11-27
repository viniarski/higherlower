import random
import art
import game_data
from replit import clear

def compare():
    score = 0
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)

    while True:
        if a != b:
            break
        else:
            b = random.choice(game_data.data)

    active = True
    while active:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        clear()
        if a['follower_count'] > b['follower_count'] and answer == "a":
            score += 1
            print(art.logo)
            print(f"\nYou're right! Current score: {score}.")
        elif b['follower_count'] > a['follower_count'] and answer == "b":
            score += 1
            print(art.logo)
            print(f"\nYou're right! Current score: {score}.")
        else:
            print(art.logo)
            print(f"\nSorry, that is wrong. Final score: {score}.")
            active = False
        a = b
        b = random.choice(game_data.data)
        while True:
            if a != b:
                break
            else:
                b = random.choice(game_data.data)


print(art.logo)
compare()

