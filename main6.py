def str2(m, resulte, resulte2):
    for x in m:
        if type(x) == int:
            resulte.append(x)

        else:
            resulte2.append(x)
    return resulte
print(str2(["A", 0, "Edabit", 6453, 1729, "Python", "1729"], [], []))