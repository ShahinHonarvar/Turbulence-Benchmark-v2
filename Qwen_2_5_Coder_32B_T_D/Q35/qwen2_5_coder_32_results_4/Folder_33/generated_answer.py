def remove_repeat_chars(s):
    if len(s) <= 826:
        return s
    section = s[126:825]
    counts = {char: section.count(char) for char in set(section)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))