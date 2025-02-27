def return_nth_smallest_ascii(s):
    characters = [c for c in s[51:90]]
    characters.sort(key=lambda x: ord(x))
    return characters[13]