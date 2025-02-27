def return_nth_smallest_ascii(input_string):
    """Return the character with the 13th smallest ASCII value in a given string between indices 5 and 47."""
    substring = input_string[5:48]
    sorted_chars = sorted(substring)
    return sorted_chars[12]