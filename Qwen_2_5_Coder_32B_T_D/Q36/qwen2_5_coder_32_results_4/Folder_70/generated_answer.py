def filter_chars(s):
    if len(s) <= 195:
        return s
    chars_to_remove = set(s[170:195])
    filtered_chars = {c for c in chars_to_remove if '!' < c < '}'}
    return ''.join((c for c in s if c not in filtered_chars))