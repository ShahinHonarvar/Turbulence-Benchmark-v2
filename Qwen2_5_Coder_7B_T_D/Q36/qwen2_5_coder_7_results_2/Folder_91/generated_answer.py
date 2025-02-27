def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(1, 4) if '$' < s[i] < '?'))
    return ''.join([char for char in s if char not in chars_to_remove])