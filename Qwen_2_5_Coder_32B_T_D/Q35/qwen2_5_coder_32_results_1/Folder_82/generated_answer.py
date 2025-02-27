def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    target = s[30:200]
    count = {char: target.count(char) for char in set(target)}
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))