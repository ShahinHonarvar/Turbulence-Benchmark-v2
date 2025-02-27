def return_nth_smallest_ascii(string):
    characters = [char for char in string[1:47]]
    sorted_characters = sorted(characters, key=lambda x: ord(x))
    return sorted_characters[12]