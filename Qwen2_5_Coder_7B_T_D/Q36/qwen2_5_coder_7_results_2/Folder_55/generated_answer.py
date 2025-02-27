def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('Y') + 1, ord('s'))]
    filtered_chars = [char for char in s if char not in target_chars]
    return ''.join(filtered_chars)