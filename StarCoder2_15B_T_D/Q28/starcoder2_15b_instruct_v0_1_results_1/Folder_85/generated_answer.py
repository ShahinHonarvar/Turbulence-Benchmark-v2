def return_nth_smallest_ascii(string):
    characters_between_indices = []
    for index, character in enumerate(string):
        if 17 <= index <= 86:
            characters_between_indices.append(character)
    ascii_values = [ord(character) for character in characters_between_indices]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[14])