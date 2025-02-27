def return_nth_smallest_ascii(input_string: str) -> str:
    characters = list(input_string)
    sorted_characters = sorted(characters[34:69], key=lambda c: ord(c))
    return sorted_characters[5]