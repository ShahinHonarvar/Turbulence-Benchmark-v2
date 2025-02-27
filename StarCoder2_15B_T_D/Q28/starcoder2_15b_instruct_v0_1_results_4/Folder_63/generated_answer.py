def return_nth_smallest_ascii(string):
    substring = string[47:71]
    characters = list(substring)
    characters.sort(key=lambda x: ord(x))
    return characters[13]