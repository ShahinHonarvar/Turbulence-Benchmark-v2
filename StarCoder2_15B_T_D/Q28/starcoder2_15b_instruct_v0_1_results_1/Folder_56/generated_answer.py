def return_nth_smallest_ascii(string):
    characters = [char for char in string if char in string[0:5]]
    characters.sort()
    return characters[3]