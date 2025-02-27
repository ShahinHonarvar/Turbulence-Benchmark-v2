def return_nth_smallest_ascii(s):
    characters = [c for c in s[63:77]]
    characters.sort(key=lambda c: ord(c))
    return characters[13]