def return_nth_smallest_ascii(s):
    characters = [c for c in s[1:32]]
    characters.sort(key=lambda x: ord(x))
    return characters[5]