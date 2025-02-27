def remove_repeat_chars(s):
    target_range = s[375:926]
    filtered_chars = {char for char in target_range if target_range.count(char) > 1}
    return ''.join((char for char in s if char not in filtered_chars or not 375 <= s.index(char) < 926))