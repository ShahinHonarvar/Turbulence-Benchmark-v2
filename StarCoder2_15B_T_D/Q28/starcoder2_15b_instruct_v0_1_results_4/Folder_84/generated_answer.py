def return_nth_smallest_ascii(string):
    characters = [c for c in string if 52 <= string.index(c) <= 79]
    characters.sort(key=lambda c: ord(c))
    return characters[6]