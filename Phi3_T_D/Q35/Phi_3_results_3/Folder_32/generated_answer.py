def remove_repeat_chars(s):
    target = s[86:90]
    seen = set(target)
    result = ''
    for i, char in enumerate(s):
        if char not in seen or target.count(char) < 2 or (not 86 <= i <= 90):
            result += char
            if char in target:
                seen.remove(char)
    return result