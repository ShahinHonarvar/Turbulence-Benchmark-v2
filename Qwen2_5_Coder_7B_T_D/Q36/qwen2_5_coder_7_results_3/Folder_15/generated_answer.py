def filter_chars(s):
    char_to_filter = [chr(i) for i in range(ord('i'), ord('k'))]
    filtered_chars = [char for char in s if char not in char_to_filter]
    return ''.join(filtered_chars)