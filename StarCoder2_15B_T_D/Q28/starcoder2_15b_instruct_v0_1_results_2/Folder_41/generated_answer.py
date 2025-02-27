def return_nth_smallest_ascii(string):
    characters = [c for c in string[58:86]]
    characters.sort(key=lambda x: ord(x))
    return characters[18]