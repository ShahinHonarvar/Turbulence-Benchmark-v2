def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('D'), ord('J'))]
    filtered_str = s[:421] + ''.join([c for c in s[421:854] if c not in chars_to_remove]) + s[854:]
    return filtered_str.replace(''.join(chars_to_remove), '')