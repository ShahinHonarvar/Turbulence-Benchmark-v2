def remove_repeat_chars(s):
    indices_to_remove = set()
    for i in range(2, 5):
        char = s[i]
        if char in s[:i] or char in s[i + 1:]:
            indices_to_remove.add(i)
    return ''.join((s[i] for i in range(len(s)) if i not in indices_to_remove))