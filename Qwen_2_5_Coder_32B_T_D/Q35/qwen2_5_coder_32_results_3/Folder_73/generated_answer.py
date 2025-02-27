def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    segment = s[10:76]
    counts = {char: segment.count(char) for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in counts))