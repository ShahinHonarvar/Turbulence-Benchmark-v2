def return_nth_smallest_ascii(string):
    characters = [char for char in string[44:70]]
    characters.sort(key=lambda c: ord(c))
    return characters[14]