def filter_chars(s):
    char_to_remove = set()
    for i in range(23, 45):
        if '3' < s[i] < 'I':
            char_to_remove.add(s[i])
    return ''.join([c for c in s if c not in char_to_remove])