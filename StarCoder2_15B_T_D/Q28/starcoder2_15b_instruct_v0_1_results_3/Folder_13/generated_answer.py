def return_nth_smallest_ascii(string):
    substring = string[47:81]
    characters = [char for char in substring]
    characters.sort(key=lambda x: ord(x))
    return characters[3]