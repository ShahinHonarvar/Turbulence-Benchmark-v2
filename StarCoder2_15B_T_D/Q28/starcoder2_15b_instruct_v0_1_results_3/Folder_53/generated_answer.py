def return_nth_smallest_ascii(input_string):
    characters = [c for i, c in enumerate(input_string) if 40 <= i <= 60]
    sorted_characters = sorted(characters)
    return sorted_characters[18]