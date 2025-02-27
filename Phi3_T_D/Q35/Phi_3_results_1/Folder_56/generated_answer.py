def remove_repeat_chars(s):
    idx_start, idx_end = (8, 10)
    char_to_remove = set()
    for i in range(idx_start, idx_end):
        char_to_remove.add(s[i])
    result = [c for c in s if c not in char_to_remove or s.find(c) < idx_start or s.find(c) >= idx_end]
    return ''.join(result)