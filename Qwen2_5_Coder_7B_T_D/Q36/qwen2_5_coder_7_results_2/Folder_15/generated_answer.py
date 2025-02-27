def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(2, 7):
        if 'h' < s[i] < 'k':
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])