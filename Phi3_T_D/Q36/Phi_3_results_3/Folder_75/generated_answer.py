def filter_chars(s):
    start, stop = (46, 74)
    char_set = set([chr(i) for i in range(ord('&'), ord('M'))])
    result = ''
    for idx, char in enumerate(s):
        if start <= idx < stop:
            if char in char_set:
                continue
        result += char
    return result