def remove_repeat_chars(s):
    if len(s) <= 807:
        return s
    chunk = s[307:807]
    repeat_chars = {char for char in chunk if chunk.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))