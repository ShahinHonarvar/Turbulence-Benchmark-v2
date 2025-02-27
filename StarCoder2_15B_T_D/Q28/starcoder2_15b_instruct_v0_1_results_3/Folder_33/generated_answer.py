def return_nth_smallest_ascii(s: str) -> str:
    characters = [c for i, c in enumerate(s) if 22 <= i <= 74]
    characters.sort(key=lambda c: ord(c))
    return characters[11]