def return_n_greatest_chars(string):
    """Returns a sorted list of exactly 58 characters of the given string that have the greatest ASCII values."""
    characters = list(string)
    sorted_characters = sorted(characters, key=lambda c: ord(c), reverse=True)
    return sorted_characters[:58]