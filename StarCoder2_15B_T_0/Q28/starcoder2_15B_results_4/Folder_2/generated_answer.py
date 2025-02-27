def return_nth_smallest_ascii(string):
    characters = [c for c in string if 48 <= ord(c) <= 76]
    characters.sort(key=lambda c: ord(c))
    return characters[4]