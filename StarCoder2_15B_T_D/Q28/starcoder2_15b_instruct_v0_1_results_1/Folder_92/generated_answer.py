def return_nth_smallest_ascii(string):
    characters = [c for c in string if c.isalpha()]
    sorted_characters = sorted(characters)
    return sorted_characters[3]