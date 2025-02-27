def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    t = s[100:200]
    count = {char: t.count(char) for char in set(t)}
    chars_to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in chars_to_remove))