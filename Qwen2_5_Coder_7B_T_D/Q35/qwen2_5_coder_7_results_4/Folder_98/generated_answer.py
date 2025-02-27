def remove_repeat_chars(s):
    counts = {}
    for i, char in enumerate(s):
        if 0 < i < 7:
            counts[char] = counts.get(char, 0) + 1
    return ''.join((char for char in s if counts.get(char) < 2 or 0 >= i >= 7))