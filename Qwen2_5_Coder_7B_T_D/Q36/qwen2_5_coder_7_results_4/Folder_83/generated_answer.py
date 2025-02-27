def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('<') + 1, ord('J'))]
    filtered_chars = [c for c in s if c not in target_chars]
    return ''.join(filtered_chars[72:93])