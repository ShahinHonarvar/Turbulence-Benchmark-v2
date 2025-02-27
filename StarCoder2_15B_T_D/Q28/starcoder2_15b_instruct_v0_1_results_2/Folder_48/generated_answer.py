def return_nth_smallest_ascii(string: str) -> str:
    characters = [c for c in string[37:60]]
    characters.sort(key=lambda c: ord(c))
    return characters[5]