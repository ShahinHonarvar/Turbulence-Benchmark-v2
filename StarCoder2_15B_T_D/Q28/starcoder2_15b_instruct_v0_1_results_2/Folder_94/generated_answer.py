def return_nth_smallest_ascii(characters):
    sorted_characters = sorted(characters)
    selected_characters = sorted_characters[6:59]
    return nth_smallest(selected_characters, 19)