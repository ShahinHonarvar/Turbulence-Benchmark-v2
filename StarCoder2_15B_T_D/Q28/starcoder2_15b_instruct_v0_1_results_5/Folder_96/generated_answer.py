def return_nth_smallest_ascii(string):
    characters = [c for c in string if 0 <= string.index(c) <= 17]
    characters.sort(key=lambda c: ord(c))
    return characters[17]