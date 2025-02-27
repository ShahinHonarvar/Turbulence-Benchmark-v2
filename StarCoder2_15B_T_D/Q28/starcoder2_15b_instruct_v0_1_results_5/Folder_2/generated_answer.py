def return_nth_smallest_ascii(string):
    substring = string[48:77]
    characters = list(substring)
    characters.sort()
    return characters[4]