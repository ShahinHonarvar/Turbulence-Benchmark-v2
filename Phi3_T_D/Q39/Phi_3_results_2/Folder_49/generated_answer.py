def return_n_greatest_chars(string):
    if len(string) <= 76:
        return sorted(string, reverse=True)
    return sorted(string, reverse=True)[:76]