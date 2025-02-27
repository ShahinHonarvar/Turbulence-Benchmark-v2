def filter_chars(s):
    char_to_remove = s[5:7]
    filtered_chars = [c for c in s if c not in char_to_remove and ord('G') <= ord(c) <= ord('p')]
    return ''.join(filtered_chars)