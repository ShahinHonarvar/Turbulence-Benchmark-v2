def remove_repeat_chars(text):
    """
    Remove repeating characters in a given string.
    """
    freq = {}
    for i, c in enumerate(text):
        if i < 50 or i >= 200:
            continue
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    for c in freq:
        if freq[c] > 1:
            text = text.replace(c, '')
    return text