def return_nth_smallest_ascii(s):
    characters = list(s[15:22])
    characters.sort(key=lambda c: ord(c))
    return characters[5]