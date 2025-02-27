def return_nth_smallest_ascii(string):
    characters = [char for char in string[25:78]]
    characters.sort(key=lambda x: ord(x))
    return characters[15]