def return_nth_smallest_ascii(s):
    characters = [c for i, c in enumerate(s) if 62 <= i <= 83]
    characters.sort(key=lambda c: ord(c))
    return characters[8]