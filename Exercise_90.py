"""Please write a program to generate all sentences where the subject is in ["I", "You"] and the verb is in ["Play",
"Love"] and the object is in ["Hockey","Football"].
Use list[index] notation to get an element from a list."""

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = []

for subject in subjects:
    for verb in verbs:
        for object in objects:
            sentences.append(f"{subject} {verb} {object}.")

print(sentences)