def return_nth_smallest_ascii(string):
    characters = [ch for ch in string[25:89]]
    characters.sort(key=lambda ch: ord(ch))
    return characters[10]