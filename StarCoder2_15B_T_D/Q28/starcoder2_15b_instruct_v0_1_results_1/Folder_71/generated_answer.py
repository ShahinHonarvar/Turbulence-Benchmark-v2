def return_nth_smallest_ascii(string: str) -> str:
    characters = [c for c in string[5:83]]
    sorted_characters = sorted(characters, key=lambda c: ord(c))
    return sorted_characters[15]