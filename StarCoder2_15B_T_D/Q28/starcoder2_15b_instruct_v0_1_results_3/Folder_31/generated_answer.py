def return_nth_smallest_ascii(string):
    substring = string[10:83]
    characters = [char for char in substring]
    characters.sort(key=lambda x: ord(x))
    return characters[17]