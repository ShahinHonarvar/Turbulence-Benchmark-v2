def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 8th smallest ASCII value among those characters in the string `s`
    that occur between indices 14 and 66, both inclusive.
    """
    sliced_chars = s[14:67]
    char_freqs = {}
    for char in sliced_chars:
        if char not in char_freqs:
            char_freqs[char] = 1
        else:
            char_freqs[char] += 1
    sorted_chars = sorted(char_freqs.items(), key=lambda x: x[1])
    return sorted_chars[7][0]