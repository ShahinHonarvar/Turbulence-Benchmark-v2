def filter_chars(s):
    filtered = [c for c in s if not (78 < ord(c) < 82 and 83 < ord(c) < 91)]
    filtered_string = ''.join(filtered)
    return filtered_string