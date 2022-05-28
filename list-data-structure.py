# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

payer_id = random.randint(0,int(len(names)-1))


print(f"Yang bayar hari ini adalah {names[payer_id]}")