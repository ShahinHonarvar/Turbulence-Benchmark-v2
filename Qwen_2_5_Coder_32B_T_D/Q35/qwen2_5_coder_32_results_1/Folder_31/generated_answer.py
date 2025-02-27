def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    part = s[34:78]
    count = {char: part.count(char) for char in set(part) if part.count(char) > 1}
    result = [char for char in s if char not in count]
    return ''.join(result)