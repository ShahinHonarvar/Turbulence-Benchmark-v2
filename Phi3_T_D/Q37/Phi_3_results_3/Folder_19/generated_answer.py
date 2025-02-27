from string import ascii_lowercase as low

def filter_chars(string):
    E_idx, t_idx = (low.index('e') + 35, low.index('t') + 35)
    chars_to_remove = low[E_idx:t_idx + 1]
    filtered_string = ''.join((char for char in string if char.lower() not in chars_to_remove or not 35 <= string.index(char) <= 89))
    return filtered_string