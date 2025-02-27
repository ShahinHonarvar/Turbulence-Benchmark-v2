def return_nth_smallest_ascii(string):
    characters = list(string)
    characters.sort(key=ord)
    return characters[8]