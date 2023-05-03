import random

city_phrases = ["Welcome to our city!", "What's with your pointy ears?", "You better watch out, there are bandits out there.", "Haven't seen you around before.", "You look familiar.",
                "Why are you so afraid of my ring?"]

def display_dialogue():
    phrase = random.choice(city_phrases)
    print(phrase)


