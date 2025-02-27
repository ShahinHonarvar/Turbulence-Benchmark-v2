def return_nth_smallest_ascii(string):
    characters = sorted(string[14:67])
    return characters[7] if len(characters) >= 8 else None