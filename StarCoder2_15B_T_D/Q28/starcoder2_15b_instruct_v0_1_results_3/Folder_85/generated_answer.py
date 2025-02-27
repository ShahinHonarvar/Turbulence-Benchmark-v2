def return_nth_smallest_ascii(string):
    characters = [ch for ch in string if ch.isalpha()]
    sorted_characters = sorted(characters, key=lambda ch: ord(ch))
    return sorted_characters[14]