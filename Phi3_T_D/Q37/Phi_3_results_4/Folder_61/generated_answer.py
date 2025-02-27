def filter_chars(s):
    target_range = s[5:7]
    filtered_chars = [char for char in s if char not in target_range and 'G' <= char <= 'p']
    return ''.join(filtered_chars)