def filter_chars(s):
    chars_to_remove = set('6789abcdefghijklmnopqrstuvw')
    filtered_chars = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered_chars)