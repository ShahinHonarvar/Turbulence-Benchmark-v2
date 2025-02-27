def return_nth_smallest_ascii(characters):
    characters_between_indices = characters[58:86]
    sorted_characters = sorted(characters_between_indices)
    return sorted_characters[18]