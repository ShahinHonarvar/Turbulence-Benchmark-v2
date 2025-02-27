def remove_repeat_chars(s):
    if len(s) <= 25:
        return s
    target = set(s[23:25])
    count = {char: 0 for char in target}
    for char in s[23:25]:
        count[char] += 1
    repeat_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeat_chars))