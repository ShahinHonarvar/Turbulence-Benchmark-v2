def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(32, 47) if '0' <= chr(i) <= 'k'}
    return ''.join((c for c in s if c not in chars_to_remove))