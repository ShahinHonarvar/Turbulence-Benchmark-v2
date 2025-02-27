def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('('), ord(']') + 1)))
    result = [c for c in string if c not in chars_to_remove]
    return ''.join(result)