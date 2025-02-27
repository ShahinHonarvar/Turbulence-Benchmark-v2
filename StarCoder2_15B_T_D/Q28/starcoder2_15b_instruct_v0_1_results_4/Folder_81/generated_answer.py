def return_nth_smallest_ascii(string):
    characters = string[:14]
    sorted_characters = sorted(characters)
    return sorted_characters[13]