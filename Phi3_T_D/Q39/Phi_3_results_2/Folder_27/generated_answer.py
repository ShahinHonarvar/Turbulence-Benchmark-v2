def return_n_greatest_chars(s):
    chars = sorted(s, reverse=True)[:82]
    if len(chars) < 82:
        fillers = [''] * (82 - len(chars))
        chars.extend(fillers)
    return chars