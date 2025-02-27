def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    t = s[42:87]
    counts = {char: t.count(char) for char in set(t)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))