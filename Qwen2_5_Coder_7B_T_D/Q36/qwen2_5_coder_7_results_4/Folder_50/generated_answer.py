def filter_chars(s):
    char_set = set(s[61:88])
    filtered_chars = [char for char in s if char not in char_set or not (char > '%' and char < 'q')]
    return ''.join(filtered_chars)