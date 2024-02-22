def showdown(p1, p2):
    if len(p1) > len(p2):
        return "p1"

    if len(p1) < len(p2):
        return "p2"

    elif len(p1) == len(p2):
        return "tie"
p1 = "         Bang!"
p2 = "              Bang!"
print(showdown(p1, p2))