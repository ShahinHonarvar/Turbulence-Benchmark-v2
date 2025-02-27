def remove_repeat_chars(s):
    sub_str = s[1:8]
    seen = set()
    result = [char for char in s if char not in sub_str or (char not in seen and (seen.add(char) or True))]
    return ''.join(result)