def return_nth_smallest_ascii(string):
    characters = []
    for c in string:
        characters.append(c)
    sorted_characters = sorted(characters)
    return sorted_characters[12]