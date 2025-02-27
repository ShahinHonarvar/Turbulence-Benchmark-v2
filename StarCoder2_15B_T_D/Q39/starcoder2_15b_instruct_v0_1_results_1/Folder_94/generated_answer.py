def return_n_greatest_chars(string):
    distinct_chars = list(set(string))
    distinct_chars.sort(key=lambda c: ord(c), reverse=True)
    return distinct_chars[:87]