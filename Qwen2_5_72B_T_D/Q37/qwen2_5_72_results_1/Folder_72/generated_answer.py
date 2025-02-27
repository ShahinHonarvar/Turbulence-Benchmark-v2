def filter_chars(s):
    chars_to_remove = set()
    for i in range(35, 52):
        if 35 <= i < len(s) and 'H' <= s[i] <= 's':
            chars_to_remove.add(s[i])
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result