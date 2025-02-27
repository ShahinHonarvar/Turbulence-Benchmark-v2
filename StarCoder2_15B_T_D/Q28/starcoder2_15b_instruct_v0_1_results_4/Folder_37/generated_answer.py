def return_nth_smallest_ascii(string):
    characters = [char for char in string[28:68]]
    characters.sort(key=lambda x: ord(x))
    return characters[14]