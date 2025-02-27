def return_nth_smallest_ascii(s):
    characters = [c for c in s[50:76]]
    characters.sort(key=lambda c: ord(c))
    return characters[6]