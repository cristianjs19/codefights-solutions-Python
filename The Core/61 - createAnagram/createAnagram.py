def createAnagram(s, t):
    l = list(t)
    for i in s:
        if i in l:
            l.remove(i)
    return len(l)
