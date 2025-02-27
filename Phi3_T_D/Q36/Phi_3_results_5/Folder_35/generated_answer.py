def filter_chars(s):
    chars_to_remove = set()
    for i in range(163, 658):
        char = s[i]
        if '(' < char < ']':
            chars_to_remove.add(char)
    filtered_list = [ch if ch not in chars_to_remove else '' for ch in s]
    return ''.join(filtered_list)