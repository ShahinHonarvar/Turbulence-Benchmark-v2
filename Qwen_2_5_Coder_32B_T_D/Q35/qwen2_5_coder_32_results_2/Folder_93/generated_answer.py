def remove_repeat_chars(s):
    target_slice = s[58:85]
    char_count = {char: target_slice.count(char) for char in set(target_slice)}
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join([char for char in s if char not in repeat_chars])