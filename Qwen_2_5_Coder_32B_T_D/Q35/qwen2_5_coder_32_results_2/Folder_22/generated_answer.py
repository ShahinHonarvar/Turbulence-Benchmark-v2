def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[51:200]
    count = {char: sub.count(char) for char in sub}
    chars_to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in chars_to_remove))