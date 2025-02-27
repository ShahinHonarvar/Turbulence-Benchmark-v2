def return_nth_smallest_ascii(s):
    characters = list(s[10:91])
    characters.sort(key=lambda c: ord(c))
    return characters[19]