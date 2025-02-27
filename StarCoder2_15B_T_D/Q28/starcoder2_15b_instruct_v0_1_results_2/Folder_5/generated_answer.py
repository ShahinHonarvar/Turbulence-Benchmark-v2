def return_nth_smallest_ascii(string):
    characters = list(string[5:90])
    characters.sort(key=lambda x: ord(x))
    return characters[12]