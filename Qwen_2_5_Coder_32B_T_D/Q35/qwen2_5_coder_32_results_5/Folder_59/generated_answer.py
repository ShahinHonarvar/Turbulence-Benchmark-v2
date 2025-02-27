def remove_repeat_chars(s):
    substring = s[1:10]
    char_count = {char: substring.count(char) for char in substring if substring.count(char) > 1}
    result = [char for char in s if char not in char_count]
    return ''.join(result)