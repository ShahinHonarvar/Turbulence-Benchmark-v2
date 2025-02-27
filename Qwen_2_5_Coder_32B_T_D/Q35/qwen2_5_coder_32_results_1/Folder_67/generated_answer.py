def remove_repeat_chars(s):
    if len(s) <= 67:
        return s
    section = s[45:67]
    counts = {char: section.count(char) for char in section}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))