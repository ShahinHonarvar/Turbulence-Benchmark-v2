def return_n_greatest_chars(string):
    """
    Takes a string of distinct characters and returns a sorted list of exactly 59 characters
    of the given string that have the greatest ASCII values.
    """
    char_freq = {}
    for char in string:
        char_freq[char] = ord(char)
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars[:59]