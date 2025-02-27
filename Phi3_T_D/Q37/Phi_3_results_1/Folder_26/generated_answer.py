def filter_chars(s, i, k):
    filtered_list = [char for index, char in enumerate(s) if not (20 <= index <= 62 and ord('i') <= ord(char) <= ord('k'))]
    filtered_str = ''.join(filtered_list)
    return filtered_str