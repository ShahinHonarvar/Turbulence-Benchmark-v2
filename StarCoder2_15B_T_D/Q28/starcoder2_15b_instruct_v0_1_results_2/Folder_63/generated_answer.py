def return_nth_smallest_ascii(s: str) -> str:
    characters = [c for c in s[47:71]]
    characters.sort(key=lambda c: ord(c))
    return characters[13]