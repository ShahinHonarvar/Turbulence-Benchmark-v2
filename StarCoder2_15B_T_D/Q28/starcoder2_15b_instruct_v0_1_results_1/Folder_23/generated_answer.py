def return_nth_smallest_ascii(string):
    characters = [char for char in string[29:48]]
    characters.sort(key=lambda c: ord(c))
    return characters[6]