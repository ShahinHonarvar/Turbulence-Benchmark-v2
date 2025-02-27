def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    substring = s[41:200]
    repeat_chars = {char for char in substring if substring.count(char) > 1}
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)