def return_nth_smallest_ascii(string):
    characters = [char for char in string[5:11]]
    characters.sort(key=lambda x: ord(x))
    return characters[5]