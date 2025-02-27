def filter_chars(s):
    if len(s) >= 80:
        chars_to_filter = set(s[78:81])
        filtered_string = ''.join([char for char in s if char not in chars_to_filter and (ord('S') <= ord(char) or ord(char) >= ord('['))])
        return filtered_string
    else:
        return s