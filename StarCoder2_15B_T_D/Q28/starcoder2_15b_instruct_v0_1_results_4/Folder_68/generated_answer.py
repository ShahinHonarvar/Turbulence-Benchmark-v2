def return_nth_smallest_ascii(string):
    """
    This function takes a string of distinct characters as input and returns the character with the 11th smallest ASCII value among those characters in the string that occur between indices 0 to 10, both inclusive.
    """
    characters = [char for char in string if ord(char) in range(ord(string[0]), ord(string[10]) + 1)]
    characters.sort(key=lambda c: ord(c))
    return characters[10]