import random
tips = []
with open("Tips.txt", "r") as file:
    for line in file:
        tip = line.strip()
        tips.append(tip)
random_tip = random.choice(tips)
print(tip)