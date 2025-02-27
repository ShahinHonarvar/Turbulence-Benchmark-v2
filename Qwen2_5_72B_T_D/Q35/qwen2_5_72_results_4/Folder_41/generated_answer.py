def remove_repeat_chars(s):
    to_remove = set()
    char_count = {}
    for i in range(3, 9):
        if s[i] in char_count:
            char_count[s[i]] += 1
            to_remove.add(s[i])
        else:
            char_count[s[i]] = 1
    result = ''.join([c for c in s if c not in to_remove])
    return result