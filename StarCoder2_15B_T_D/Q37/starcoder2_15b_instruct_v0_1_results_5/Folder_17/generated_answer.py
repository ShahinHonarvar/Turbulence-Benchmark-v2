def filter_chars(string):
    string_chars = list(string)
    filtered_chars = [c for c in string_chars if not 27 <= ord(c) - ord(';') <= 29]
    return ''.join(filtered_chars)