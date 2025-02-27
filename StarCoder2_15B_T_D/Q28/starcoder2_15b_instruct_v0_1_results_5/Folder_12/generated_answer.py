def return_nth_smallest_ascii(string):
    characters = [c for c in string if 3 <= string.index(c) <= 26]
    sorted_characters = sorted(characters, key=lambda c: ord(c))
    return sorted_characters[4]