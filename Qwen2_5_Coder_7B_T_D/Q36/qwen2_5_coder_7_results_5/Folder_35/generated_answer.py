def filter_chars(s):
    filtered_chars = set(s[163:658])
    result = ''.join([ch for ch in s if ch not in filtered_chars or ch <= '(' or ch >= ']'])
    return result