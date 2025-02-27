def return_nth_smallest_ascii(string):
    substring = string[50:76]
    characters = list(substring)
    characters.sort(key=lambda c: ord(c))
    return characters[6]