def remove_repeat_chars(s):
    substring = s[7:9]
    chars_to_remove = {char for char in substring if substring.count(char) > 1}
    result = [char for char in s if char not in chars_to_remove or char not in substring]
    return ''.join(result)