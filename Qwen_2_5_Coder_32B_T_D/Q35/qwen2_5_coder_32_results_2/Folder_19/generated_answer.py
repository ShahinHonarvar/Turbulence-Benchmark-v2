def remove_repeat_chars(s):
    substring = s[1:5]
    char_count = {char: substring.count(char) for char in substring}
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))