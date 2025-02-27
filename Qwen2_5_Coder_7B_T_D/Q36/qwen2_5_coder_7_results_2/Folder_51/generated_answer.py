def filter_chars(s):
    indices_to_remove = {i for i in range(58, 81) if '5' < s[i] < '>'}
    result = ''.join((char for char in s if char not in indices_to_remove))
    return result