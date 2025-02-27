def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    count = {}
    for i in range(61, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((c for c in s if c not in remove_chars))