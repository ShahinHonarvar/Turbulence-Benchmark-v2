def filter_chars(s):
    start_idx = 46
    end_idx = 74
    exclude_list = [chr(i) for i in range(ord('&'), ord('M'))]
    result = ''
    for i, char in enumerate(s):
        if start_idx <= i < end_idx and char in exclude_list:
            continue
        result += char
    return result