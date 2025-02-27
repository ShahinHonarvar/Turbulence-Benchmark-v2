def return_nth_smallest_ascii(string: str) -> str:
    if not isinstance(string, str) or len(string) == 0:
        return None
    characters = list(string)
    characters.sort(key=lambda c: ord(c))
    characters = characters[9:23]
    if len(characters) < 4:
        return None
    return characters[3]