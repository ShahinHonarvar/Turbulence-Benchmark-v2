def remove_repeat_chars(s):
    to_remove = set()
    for i in range(39, 43):
        if s[i] in s[39:i] + s[i + 1:43]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result