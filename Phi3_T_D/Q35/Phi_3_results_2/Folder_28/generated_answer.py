def remove_repeat_chars(s):
    substring = s[86:99]
    seen_chars = set()
    repeated_chars = set([char for char in substring if substring.count(char) > 1])
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
    return result