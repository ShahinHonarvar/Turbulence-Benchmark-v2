def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    part = s[45:91]
    counts = {char: part.count(char) for char in set(part)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))