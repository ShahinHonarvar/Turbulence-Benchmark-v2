def remove_repeat_chars(s):
    if len(s) <= 807:
        return s
    temp = s[306:807]
    char_count = {char: temp.count(char) for char in set(temp) if temp.count(char) > 1}
    return ''.join([char for char in s if char not in char_count])