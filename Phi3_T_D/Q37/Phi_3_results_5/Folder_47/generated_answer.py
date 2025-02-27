def filter_chars(s):
    filtered_str = []
    char_set = set(':r') | set(s[37:55])
    for char in s:
        if char in char_set:
            if ':' <= char <= 'r':
                char_set.remove(char)
            continue
        filtered_str.append(char)
    return ''.join(filtered_str)