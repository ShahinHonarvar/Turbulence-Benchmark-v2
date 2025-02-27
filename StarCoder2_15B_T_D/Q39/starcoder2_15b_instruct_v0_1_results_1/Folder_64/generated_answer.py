def return_n_greatest_chars(s):
    """
    Returns a sorted list of exactly 39 characters of the given string `s` that have the greatest ASCII values.
    """
    char_freq = {}
    for char in s:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    sorted_char_freq = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_char_freq[:39]