def remove_repeat_chars(s):
    if len(s) <= 82:
        return s
    sub = s[39:81]
    count = {char: sub.count(char) for char in sub}
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))