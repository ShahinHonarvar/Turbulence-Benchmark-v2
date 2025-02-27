def return_nth_smallest_ascii(string):
    characters = [char for char in string[12:56]]
    sorted_characters = sorted(characters)
    return sorted_characters[16]