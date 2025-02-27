def return_nth_smallest_ascii(string: str) -> str:
    characters = [char for char in string if 38 <= ord(char) <= 64]
    characters.sort(key=lambda x: ord(x))
    return characters[13]