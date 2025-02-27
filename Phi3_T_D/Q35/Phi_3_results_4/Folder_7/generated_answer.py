def remove_repeat_chars(s):
    target_chars = {char for char in s[375:926] if s[375:926].count(char) > 1}
    return ''.join((char for char in s if char not in target_chars))