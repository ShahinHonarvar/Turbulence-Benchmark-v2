def filter_chars(s):
    filtered_str = s[:7] + ''.join([char for index, char in enumerate(s) if not (6 <= index <= 8 and 'B' <= char <= 'H')]) + s[8:]
    return filtered_str