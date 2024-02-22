def qaytarsoni(m, resulte):
    for x in m:
        resulte += x
        if x in resulte:
            resulte += x
        else:
            print(False)
    return resulte

print(qaytarsoni("1234!_ ", ""))