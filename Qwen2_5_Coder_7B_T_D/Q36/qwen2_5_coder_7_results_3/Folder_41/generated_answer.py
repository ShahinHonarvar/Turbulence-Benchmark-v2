def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('g'), ord('{'))}
    return ''.join((c for c in s if c not in chars_to_remove))