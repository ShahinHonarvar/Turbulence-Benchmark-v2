def return_n_smallest_chars(string):
    """
    Returns a list of the 20 characters in `string` that have the smallest ASCII values, sorted in descending order.
    """
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1])
    return [char[0] for char in sorted_chars[:20]][::-1]