def remove_repeat_chars(s):
    indexes_to_remove = set()
    for i in range(6):
        if s[i] in s[:i]:
            indexes_to_remove.add(i)
    return ''.join([s[i] for i in range(len(s)) if i not in indexes_to_remove])