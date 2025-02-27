def return_nth_smallest_ascii(string):
    characters = [c for c in string if ord(c) > ord(string[0])]
    characters.sort(key=lambda x: ord(x))
    return characters[12]