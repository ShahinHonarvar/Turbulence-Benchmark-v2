def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=lambda x: ord(x), reverse=True)
    sorted_chars = sorted(chars[:76])
    return sorted_chars