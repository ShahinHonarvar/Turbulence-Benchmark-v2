def return_nth_smallest_ascii(s):
    characters = [c for c in s if 32 <= ord(c) <= 67]
    characters.sort(key=lambda c: ord(c))
    return characters[11]