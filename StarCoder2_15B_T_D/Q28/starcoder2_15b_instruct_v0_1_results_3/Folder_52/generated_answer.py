def return_nth_smallest_ascii(string):
    characters = [char for char in string[46:73]]
    characters.sort(key=ord)
    return characters[14]