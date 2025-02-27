def filter_chars(s):
    chars_to_filter = [chr(i) for i in range(ord('%') + 1, ord('q'))]
    filtered_chars = [char for char in s if char not in chars_to_filter]
    return ''.join(filtered_chars)