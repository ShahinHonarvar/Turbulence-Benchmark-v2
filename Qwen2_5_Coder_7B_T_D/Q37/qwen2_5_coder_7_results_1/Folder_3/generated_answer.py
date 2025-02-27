def filter_chars(s):
    filtered_chars = set()
    for i in range(37, 57):
        if '6' <= s[i] <= '_':
            filtered_chars.add(s[i])
    return ''.join([c for c in s if c not in filtered_chars])