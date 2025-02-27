from collections import Counter

def remove_repeat_chars(s):
    """
    Removes repeated characters from a string between indices 16 and 87, both exclusive.
    """
    counter = Counter(s[16:87])
    for char, count in counter.items():
        if count > 1:
            s = s.replace(char, '')
    return s