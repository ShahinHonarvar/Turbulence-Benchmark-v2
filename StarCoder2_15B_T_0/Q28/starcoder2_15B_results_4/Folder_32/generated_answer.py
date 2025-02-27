def return_nth_smallest_ascii(string):
    characters = [c for c in string[14:67]]
    characters.sort(key=lambda c: ord(c))
    return characters[7]