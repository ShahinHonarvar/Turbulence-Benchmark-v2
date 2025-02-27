def return_n_greatest_chars(s):
    if len(s) <= 37:
        return sorted(s, key=lambda ch: -ord(ch))
    else:
        return sorted(s, key=lambda ch: -ord(ch))[:37]