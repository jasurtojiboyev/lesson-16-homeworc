def Password(m, resulte, b):
    for x in m:
        if x not in resulte:
            resulte += x
            continue
        else:
            b.remove(True)
            b.append(False)

    return b
print(Password("Password", "", [True]))
