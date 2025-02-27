def remove_repeat_chars(s):
    start, end = (355, 988)
    seen = {}
    to_remove = set()
    for i in range(start, end):
        char = s[i]
        if char in seen:
            seen[char] += 1
            to_remove.add(char)
        else:
            seen[char] = 1
    return ''.join((c for c in s if c not in to_remove))