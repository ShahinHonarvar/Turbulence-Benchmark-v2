def return_n_greatest_chars(s: str) -> str:
    """
    Returns a sorted list of exactly 28 characters of the given string `s` that have the greatest ASCII values.
    """
    char_freq = {}
    for c in s:
        if c not in char_freq:
            char_freq[c] = 1
        else:
            char_freq[c] += 1
    sorted_chars = sorted(char_freq.keys(), key=lambda x: ord(x), reverse=True)
    return sorted_chars[:28]