def remove_repeat_chars(s):
    start, end = (36, 52)
    chars_to_remove = set()
    for i in range(start + 1, end):
        if s[i] == s[i - 1]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))