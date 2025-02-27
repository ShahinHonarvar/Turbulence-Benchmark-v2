def return_n_greatest_chars(s):
    if len(s) <= 72:
        return sorted(s, reverse=True)
    return sorted(sorted(s, reverse=True)[:72], reverse=True)