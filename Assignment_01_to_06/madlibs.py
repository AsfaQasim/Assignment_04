def madlibs():
    print("Let's play madlibs! Fill in the blanks with your own words.\n")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_obj = input("Give me a funny object: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f"""
Once upon a time, in a place called {place}, there lived a person named {name}.
One day, they found a {funny_obj}, and that's when everything changed!
The {funny_obj} could {action_verb} and even talk. "{funny_exclamation}!" it shouted.
From that day on, {name}'s life was filled with adventure, laughter, and the most unexpected surprises.
"""

    print("\n Here is your madlibs story:")
    print(story)


madlibs()
