import random
import choice

questions = ["Why is the sky blue? ",
             "Why is Python so ez? ",
             "Where is mom? "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh...okay")
