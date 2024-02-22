def string(string1, string2):
    b = 0
    n = []
    for x in string1:
        if x in string2:
            b += 1
            n.append(b)


    return len(n)
print(string("abcdeq","bcdefa"))