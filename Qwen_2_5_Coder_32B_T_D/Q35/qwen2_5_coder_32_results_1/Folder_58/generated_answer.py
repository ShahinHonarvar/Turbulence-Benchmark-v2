def remove_repeat_chars(s):
    if len(s) <= 802:
        return s
    count = {}
    for i in range(104, 802):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join([char for char in s if char not in to_remove])