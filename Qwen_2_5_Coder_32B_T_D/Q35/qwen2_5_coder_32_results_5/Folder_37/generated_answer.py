def remove_repeat_chars(s):
    substr = s[2:7]
    char_count = {char: substr.count(char) for char in set(substr)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))