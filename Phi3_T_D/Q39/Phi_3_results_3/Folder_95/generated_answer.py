def return_n_greatest_chars(s):
    ascii_vals = sorted([ord(char) for char in s if len(s) >= 36], reverse=True)[:36]
    return sorted(ascii_vals)