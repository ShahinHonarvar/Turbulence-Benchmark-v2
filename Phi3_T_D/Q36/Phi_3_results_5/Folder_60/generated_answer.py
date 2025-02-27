def filter_chars(s):
    sub_string = s[23:83]
    filtered_chars = [c for c in sub_string if not 'f' < c < 'o']
    return s[:23] + ''.join(filtered_chars) + s[83:]