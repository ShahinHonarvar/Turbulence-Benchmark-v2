def remove_repeat_chars(s):
    target_str = s[72:93]
    to_remove = {char for char in target_str if target_str.count(char) > 1}
    result_str = s[:72] + ''.join((char for char in target_str if char not in to_remove)) + s[93:]
    return result_str