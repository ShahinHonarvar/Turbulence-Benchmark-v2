def remove_repeat_chars(s):
    if len(s) <= 826:
        return s
    substr = s[126:825]
    counts = {char: substr.count(char) for char in substr}
    remove_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in remove_chars))