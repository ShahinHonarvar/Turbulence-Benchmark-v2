def filter_chars(s):
    chars_to_remove = set()
    for i in range(max(114, len(s)), min(639, len(s)) + 1):
        if '!' <= s[i] <= 'x':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))