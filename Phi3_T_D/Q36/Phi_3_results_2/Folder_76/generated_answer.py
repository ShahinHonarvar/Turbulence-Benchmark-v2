def filter_chars(s):
    altered_str = s[:669]
    for char in s[669:888]:
        if 'B' < char < 'Y':
            altered_str += char
    altered_str += s[888:]
    return altered_str