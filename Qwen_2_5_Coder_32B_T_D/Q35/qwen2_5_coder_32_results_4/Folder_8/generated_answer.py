def remove_repeat_chars(s):
    if len(s) <= 48:
        return s
    target = s[46:48]
    count = {char: target.count(char) for char in set(target) if target.count(char) > 1}
    return ''.join([char for char in s if char not in count])