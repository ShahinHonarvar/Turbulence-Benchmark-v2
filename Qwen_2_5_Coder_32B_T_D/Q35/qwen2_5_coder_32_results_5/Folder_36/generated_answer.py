def remove_repeat_chars(s):
    if len(s) <= 709:
        return s
    temp = s[477:709]
    repeat_chars = {char for char in temp if temp.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))