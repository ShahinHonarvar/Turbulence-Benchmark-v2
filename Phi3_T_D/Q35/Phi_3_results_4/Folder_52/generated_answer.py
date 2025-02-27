def remove_repeat_chars(s):
    substring = s[38:81]
    seen = set()
    result = [char for char in s if not (char in substring and char in seen or seen.add(char))]
    return ''.join(result)