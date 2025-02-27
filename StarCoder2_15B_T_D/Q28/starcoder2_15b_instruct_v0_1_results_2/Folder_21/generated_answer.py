def return_nth_smallest_ascii(s):
    characters = list(s[8:66])
    characters.sort(key=lambda c: ord(c))
    return characters[5]