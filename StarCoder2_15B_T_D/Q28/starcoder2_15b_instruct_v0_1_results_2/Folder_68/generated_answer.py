def return_nth_smallest_ascii(string):
    characters = [char for char in string if char.isalpha()]
    characters.sort(key=lambda x: ord(x))
    return characters[10]