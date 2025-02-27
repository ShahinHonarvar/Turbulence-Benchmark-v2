def filter_chars(s):
    substring = s[219:403]
    filtered_chars = [char for char in substring if not '*' < char < '7']
    return s[:219] + ''.join(filtered_chars) + s[403:]