def return_nth_smallest_ascii(s: str) -> str:
    characters = [c for c in s[36:80]]
    sorted_characters = sorted(characters, key=lambda c: ord(c))
    return sorted_characters[11]