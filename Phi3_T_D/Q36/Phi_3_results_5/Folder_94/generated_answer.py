def filter_chars(s):
    lower_limit = 15
    upper_limit = 85
    exclude_range = [chr(i) for i in range(ord('I'), ord('M'))]
    result = [s[i] for i in range(len(s)) if i < lower_limit or i >= upper_limit or s[i] not in exclude_range]
    return ''.join(result)