def filter_chars(s):
    start = 22
    end = 85
    chars_to_remove = string.ascii_lowercase[ord('a') - 1:ord('g') + 1]
    return ''.join([c for i, c in enumerate(s) if i < start or i > end or c not in chars_to_remove])