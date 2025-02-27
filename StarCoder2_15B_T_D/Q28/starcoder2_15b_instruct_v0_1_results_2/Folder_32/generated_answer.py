def return_nth_smallest_ascii(string):
    characters_between_indices = [char for char in string[14:67]]
    sorted_characters = sorted(characters_between_indices, key=lambda char: ord(char))
    return sorted_characters[7]