def return_nth_smallest_ascii(string):
    characters = [c for c in string if 25 <= string.index(c) <= 64]
    characters.sort(key=lambda x: ord(x))
    return characters[5]