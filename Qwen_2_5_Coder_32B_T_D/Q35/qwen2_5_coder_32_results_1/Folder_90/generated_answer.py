def remove_repeat_chars(s):
    if len(s) <= 807:
        return s
    sub = s[307:807]
    counts = {char: sub.count(char) for char in set(sub)}
    repeat_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))