def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(32, 47) if chr(i) >= '0' and chr(i) <= 'k'))
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)