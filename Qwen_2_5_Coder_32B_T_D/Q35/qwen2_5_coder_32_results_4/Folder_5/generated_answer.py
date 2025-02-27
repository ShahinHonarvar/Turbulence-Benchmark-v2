def remove_repeat_chars(s):
    if len(s) < 9:
        return s
    slice_to_check = s[3:8]
    chars_to_remove = {char for char in slice_to_check if slice_to_check.count(char) > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)