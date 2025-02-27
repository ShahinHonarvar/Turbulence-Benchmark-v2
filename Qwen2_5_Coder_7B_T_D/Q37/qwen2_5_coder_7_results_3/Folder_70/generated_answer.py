def filter_chars(s):
    return ''.join([char for char in s if 515 <= s.find(char) <= 538 and (not '+' <= char <= '}')])