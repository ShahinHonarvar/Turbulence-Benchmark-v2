def return_nth_smallest_ascii(string):
    characters = [char for char in string[33:61]]
    characters.sort(key=lambda c: ord(c))
    return characters[17]