def return_nth_smallest_ascii(string: str) -> str:
    characters_between_indices = [character for index, character in enumerate(string) if 51 <= index <= 78]
    characters_between_indices.sort(key=lambda character: ord(character))
    return characters_between_indices[8]