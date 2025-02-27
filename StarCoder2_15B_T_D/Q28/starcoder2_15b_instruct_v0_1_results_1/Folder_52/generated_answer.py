def return_nth_smallest_ascii(s):
    """
    Write a function called'return_nth_smallest_ascii' that takes one argument, a string of distinct characters.
    The function should return the character with the 15th smallest ASCII value among those characters in the string
    that occur between indices 46 to 72, both inclusive.
    """
    return sorted(s[46:73])[14]