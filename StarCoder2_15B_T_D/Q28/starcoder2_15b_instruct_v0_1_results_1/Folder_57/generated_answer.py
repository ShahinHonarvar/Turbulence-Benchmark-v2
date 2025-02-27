def return_nth_smallest_ascii(s: str) -> str:
    characters = [c for i, c in enumerate(s) if 17 <= i <= 34]
    characters.sort(key=lambda c: ord(c))
    return characters[17]