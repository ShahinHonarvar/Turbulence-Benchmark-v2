def return_nth_smallest_ascii(input_string: str) -> str:
    characters_in_range = [c for c in input_string[0:45]]
    sorted_characters = sorted(characters_in_range)
    return sorted_characters[9]