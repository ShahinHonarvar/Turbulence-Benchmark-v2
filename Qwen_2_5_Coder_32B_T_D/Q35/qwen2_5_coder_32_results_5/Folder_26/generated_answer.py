def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    section = s[69:99]
    counts = {char: section.count(char) for char in set(section) if section.count(char) > 1}
    return ''.join((char for char in s if char not in counts))