def filter_chars(s):
    altered = [char for char in s if not 35 <= s.find(char) <= 98 or not 'A' <= char <= 'b']
    return ''.join(altered)