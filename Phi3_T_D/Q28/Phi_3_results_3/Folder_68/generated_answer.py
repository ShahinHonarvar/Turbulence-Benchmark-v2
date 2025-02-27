def return_nth_smallest_ascii(s):
    characters = list(s[:11])
    characters.sort(key=ord)
    return characters[10] if len(characters) >= 11 else ''