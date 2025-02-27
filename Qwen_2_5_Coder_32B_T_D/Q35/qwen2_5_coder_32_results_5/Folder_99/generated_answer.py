def remove_repeat_chars(s):
    if len(s) <= 905:
        return s
    temp = s[451:905]
    chars_to_remove = {c for c in temp if temp.count(c) > 1}
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)