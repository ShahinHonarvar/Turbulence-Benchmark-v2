def return_nth_smallest_ascii(string):
    characters = list(string[46:83])
    characters.sort(key=lambda c: ord(c))
    return characters[15]