def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('4'), ord('B') - 1)]
    return ''.join([c for i, c in enumerate(s) if i not in range(18, 64) or c not in char_to_remove])