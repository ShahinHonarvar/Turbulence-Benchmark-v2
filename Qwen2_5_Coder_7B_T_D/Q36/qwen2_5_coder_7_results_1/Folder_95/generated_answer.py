def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('+') + 1, ord('w'))]
    filtered_chars = [char for char in s if char not in chars_to_remove]
    return ''.join(filtered_chars)