def return_nth_smallest_ascii(s):
    characters = [c for c in s[35:53]]
    characters.sort(key=lambda c: ord(c))
    return characters[9]