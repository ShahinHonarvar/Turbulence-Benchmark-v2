def return_nth_smallest_ascii(string):
    """
    Returns the character with the 15th smallest ASCII value among those characters
    in the string that occur between indices 28 to 67, both inclusive.
    """
    characters = [c for c in string[28:68]]
    characters.sort(key=ord)
    return characters[14]