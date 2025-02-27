def remove_repeat_chars(s):
    if len(s) <= 80:
        return s
    check_area = s[26:80]
    char_count = {char: check_area.count(char) for char in check_area if check_area.count(char) > 1}
    result = ''.join((char for char in s if char not in char_count))
    return result