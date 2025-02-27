def return_nth_smallest_ascii(string: str) -> str:
    characters = [c for c in string[33:61]]
    characters.sort(key=lambda x: ord(x))
    return characters[17]