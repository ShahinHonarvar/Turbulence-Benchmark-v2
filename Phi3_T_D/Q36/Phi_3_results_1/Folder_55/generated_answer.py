def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 3 and i < 5:
            if 'Y' < s[i] < 's':
                continue
        filtered_string += s[i]
    return filtered_string