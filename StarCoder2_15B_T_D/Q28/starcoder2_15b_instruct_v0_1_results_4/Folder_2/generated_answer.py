def return_nth_smallest_ascii(string):
    characters = [c for c in string if 48 <= ord(c) <= 76]
    characters.sort()
    return characters[4]