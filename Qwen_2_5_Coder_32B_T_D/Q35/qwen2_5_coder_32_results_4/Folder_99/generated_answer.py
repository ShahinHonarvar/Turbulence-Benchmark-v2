def remove_repeat_chars(s):
    if len(s) <= 905:
        return s
    substring = s[451:905]
    char_count = {char: substring.count(char) for char in substring}
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))